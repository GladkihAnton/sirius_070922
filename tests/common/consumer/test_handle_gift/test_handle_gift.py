import pytest
from pathlib import Path

from consumer.app import start_consumer
from consumer.schema.gift import GiftMessage
from tests.mocking.rabbit import MockExchange

BASE_DIR = Path(__file__).parent
SEED_DIR = BASE_DIR / 'seeds'


@pytest.mark.parametrize(
    ('predefined_queue', 'seeds'),
    [
        (
            GiftMessage(event='gift', action='get_gifts', user_id=1),
            [SEED_DIR / 'public.gift.json'],
        ),
    ]
)
@pytest.mark.asyncio()
@pytest.mark.usefixtures('_load_queue', '_load_seeds')
async def test_handle_gift(mock_exchange: MockExchange) -> None:
    await start_consumer()


    # aio_pika.Message(
    #     msgpack.packb({
    #         'name': gift.name,
    #         'photo': gift.photo,
    #         'category': gift.category,
    #     }),
    #     correlation_id=correlation_id_ctx.get(),
    # ),
    # routing_key = settings.USER_GIFT_QUEUE_TEMPLATE.format(user_id=message['user_id']),
    #
    # )
    # TODO

    mock_exchange.assert_has_calls('publish', )


