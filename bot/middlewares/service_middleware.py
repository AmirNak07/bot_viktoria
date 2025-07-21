from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from bot.services.event_service import EventService


class ServiceMiddleware(BaseMiddleware):
    def __init__(self, service: EventService) -> None:
        super().__init__()
        self.service = service

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data["service"] = self.service
        return await handler(event, data)
