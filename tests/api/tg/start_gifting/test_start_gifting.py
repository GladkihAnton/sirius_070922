from datetime import datetime

import pytest
from pathlib import Path

from aiogram.types import Message, User, Chat

from src.handlers.message.gift import start_gifting

BASE_DIR = Path(__file__).parent
SEED_DIR = BASE_DIR / 'seeds'
SEED_DIR1 = BASE_DIR / 'seeds1'


@pytest.mark.parametrize(
    ('predefined_queue', 'expected_result'),
    [
        (
            {'test': 'test'},
            'expected_result',
        ),
    ]
)
@pytest.mark.asyncio()
async def test_start_gifting(expected_result) -> None:
    chat = Chat(id=1, type='private')
    user = User(id=1, is_bot=False, is_premium=False, last_name='test', first_name='test')
    message = Message(message_id=1, date=datetime.now(), chat=chat, from_user=user)

    await start_gifting(message, state=1)
