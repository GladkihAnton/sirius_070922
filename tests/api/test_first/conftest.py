from contextlib import asynccontextmanager
from pathlib import Path
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncConnection

from scripts.load_fixture import load_fixture
from src.model.gift import Gift
from src.storage.db import async_session, engine, get_db


@pytest_asyncio.fixture()
async def db_session(app: FastAPI) -> AsyncSession:
    async with engine.begin() as conn:  # start transaction
        session_maker = async_sessionmaker(bind=conn, class_=AsyncSession)  # create sessio_maker through transcation

        async with session_maker() as session:
            async def overrided_db_session() -> AsyncGenerator[AsyncSession, None]:
                yield session

            app.dependency_overrides[get_db] = overrided_db_session

            yield session
        await conn.rollback()


@pytest_asyncio.fixture()
async def _load_seeds(db_session: AsyncSession, seeds: list[Path]) -> None:
    await load_fixture(seeds, db_session)
