from .base import BaseMessage


class GiftMessage(BaseMessage):
    action: str
    user_id: int
