import traceback
from collections.abc import Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.exceptions import TelegramAPIError
from aiogram.types import TelegramObject, Update
from aiogram_dialog.api.exceptions import DialogsError
from pymongo.errors import PyMongoError

from nats.aio.errors import ErrConnectionClosed, ErrNoServers, ErrTimeout


class GlobalErrorMiddleware(BaseMiddleware):
    async def __call__(
        self, handler: Callable[..., Any], event: TelegramObject, data: dict[str, Any]
    ) -> Any:
        try:
            return await handler(event, data)
        except TelegramAPIError as e:
            print(f"[Telegram API Error] {e}")
        except DialogsError as e:
            print(f"[Dialog Error] {e}")
        except PyMongoError as e:
            print(f"[MongoDB Error] {e}")
        except (ErrConnectionClosed, ErrTimeout, ErrNoServers) as e:
            print(f"[NATS Error] {e}")
        except Exception as e:
            print(f"[Unexpected Error] {e}")
            traceback.print_exc()

        # Optional: уведомление пользователя
        if isinstance(event, Update):
            message = getattr(event, "message", None)
            if message:
                try:
                    await message.answer("Упс, что-то пошло не так... Попробуй позже.")
                except Exception:
                    pass
