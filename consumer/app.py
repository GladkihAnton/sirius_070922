import logging.config

import aio_pika
import msgpack

from consumer.handlers.gift import handle_event_gift
from consumer.logger import LOGGING_CONFIG, logger, correlation_id_ctx
from consumer.schema.gift import GiftMessage
from consumer.storage.rabbit import channel_pool


async def main() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)
    logger.info('Starting consumer...')

    queue_name = "user_messages"
    async with channel_pool.acquire() as channel:  # type: aio_pika.Channel

        # Will take no more than 10 messages in advance
        await channel.set_qos(prefetch_count=10)

        # Declaring queue
        queue = await channel.declare_queue(queue_name, durable=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter: # type: aio_pika.Message
                async with message.process():  # после выхода из with будет ack (есть еще no_ack)
                    correlation_id_ctx.set(message.correlation_id)
                    logger.info("Message ...")

                    body: GiftMessage = msgpack.unpackb(message.body)
                    if body['event'] == 'gift':
                        await handle_event_gift(body)


# Возможно более понятный код вида консмура
# queue: Queue
# while True:
#     message = await queue.get()
#     async with message.process():  # после выхода из with будет ack (есть еще no_ack)
#         correlation_id_ctx.set(message.correlation_id)
#         logger.info("Message ...")
#
#         body: GiftMessage = msgpack.unpackb(message.body)
#         if body['event'] == 'gift':
#             await handle_event_gift(body)
