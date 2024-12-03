import asyncio
from unittest.mock import AsyncMock

import msgpack


class Message(AsyncMock):
    def __init__(self, body, **kwargs):
        super().__init__(**kwargs)
        self.body = msgpack.packb(body)


    def return_body(self):
        return self.body

async def main():
    mock_message = Message(body={'test': 'test'})
    print(msgpack.unpackb(mock_message.return_body()))
    await mock_message.answer(test=1)
    x = 1


if __name__ == '__main__':
    asyncio.run(main())
