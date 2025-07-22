from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from bot.services.event_service import EventService
from bot.services.user_service import UsersService


class ServiceMiddleware(BaseMiddleware):
    def __init__(self, event_service: EventService, user_service: UsersService) -> None:
        super().__init__()
        self.event_service = event_service
        self.user_service = user_service

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data["event_service"] = self.event_service
        data["user_service"] = self.user_service
        return await handler(event, data)
