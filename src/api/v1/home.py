from fastapi import Depends
from fastapi.responses import JSONResponse, ORJSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .router import router
from src.storage.db import get_db

from ...model.gift import Gift


@router.get("/home")
async def home(session: AsyncSession = Depends(get_db)) -> JSONResponse:
    row = (await session.scalars(select(Gift))).first()
    return ORJSONResponse({"gift": {
        'id': row.id,
        'name': row.name,
        'photo': row.photo,
        'category': row.category,
    }})
# 4397111120 in get_db
# 4397111120 in helath
# 4691819984 in db_session in pytest
