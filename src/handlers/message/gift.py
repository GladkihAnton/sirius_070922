import asyncio
import json

import msgpack
from aio_pika import Queue
from aio_pika.exceptions import QueueEmpty
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F

from config.settings import settings
from ..buttons import START_GIFTING


from .router import router
from ..states.gift import GiftGroup
from ...storage.rabbit import channel_pool


# @router.message(GiftGroup.gifting)
# async def gifting(message: Message, state: FSMContext) -> None:
#     await message.answer('ypa')


@router.message(F.text == START_GIFTING)
async def start_gifting(message: Message, state: FSMContext) -> None:
    await message.answer('ypa')
    await state.set_state(GiftGroup.gifting)

    async with channel_pool.acquire() as channel:  # type: aio_pika.Channel
        queue: Queue = await channel.declare_queue(
            settings.USER_GIFT_QUEUE_TEMPLATE.format(user_id=message.from_user.id),
            durable=True,
        )

        retries = 3
        for _ in range(retries):
            try:
                gift = await queue.get()
                parsed_gift = msgpack.unpackb(gift.body)
                await message.answer(json.dumps(parsed_gift))
                return
            except QueueEmpty:
                await asyncio.sleep(1)

        await message.answer('Нет подарков')
