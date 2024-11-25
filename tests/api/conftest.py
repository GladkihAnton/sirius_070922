from pathlib import Path
from typing import AsyncGenerator
from unittest.mock import MagicMock, AsyncMock

import pytest
import pytest_asyncio
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from scripts.load_fixture import load_fixture
from src import bot
from src.storage import redis
from src.storage.db import engine, get_db
from tests.mocking.redis import MockRedis


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


@pytest_asyncio.fixture(autouse=True)
async def _mock_redis(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(redis, 'redis_storage', MockRedis())
    yield


@pytest_asyncio.fixture(autouse=True)
async def mock_bot_dp(monkeypatch: pytest.MonkeyPatch) -> AsyncMock:
    mock = AsyncMock()
    monkeypatch.setattr(bot, 'dp', mock) # bot.dp -> mock
    return mock
