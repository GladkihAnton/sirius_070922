from fastapi import Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response

from src.api.tech.router import router
from src.model.gift import Gift
from src.storage.db import get_db


@router.get("/health")
async def health(session: AsyncSession = Depends(get_db)) -> Response:
    gifts = (await session.scalars(select(Gift))).all()
    return ORJSONResponse(
        [
            {
                'id': gift.id,
                'category': gift.category,
                'photo': gift.photo,
                'name': gift.name,
            } for gift in gifts
        ]
    )
