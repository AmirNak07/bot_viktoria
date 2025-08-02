from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class ServiceMiddleware(BaseMiddleware):
    def __init__(self, services: dict[str, Any]) -> None:
        super().__init__()
        self.services = services

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data.update(self.services)
        return await handler(event, data)
