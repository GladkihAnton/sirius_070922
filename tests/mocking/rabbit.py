from collections import deque
from dataclasses import dataclass

@dataclass
class MockChannelPool:  # -> Channel
    channel: 'MockChannel'

    def acquire(self):
        return self.channel


@dataclass
class MockChannel:
    queue: 'MockQueue'

    def __aenter__(self) -> 'MockChannel':
        return self

    def __await__(self) -> 'MockChannel':
        yield
        return self

    def __aexit__(self) -> None:
        return


    async def declare_queue(self, *args, **kwargs) -> 'MockQueue':
        return self.queue


@dataclass
class MockQueue:
    queue: deque['MockMessage']

    async def get(self, *args, **kwargs) -> 'MockMessage':
        return self.queue.popleft()


    async def put(self, value: bytes) -> None:
        self.queue.append(MockMessage(body=value))


@dataclass
class MockMessage:
    body: bytes
