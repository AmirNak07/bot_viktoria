from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from bot.services.user_service import UsersService


class UserCheckMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        user: User | None = data.get("event_from_user")

        if not user:
            return await handler(event, data)

        user_service: UsersService = data["user_service"]
        user_in_db = await user_service.find_user(user.id)

        if not user_in_db:
            await user_service.insert_user(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
                is_new=True,
            )
            data["is_new_user"] = True
        else:
            data["is_new_user"] = False

        return await handler(event, data)
