from functools import wraps
from typing import Any

from pymongo.errors import PyMongoError


def handle_mongo_errors(default: Any = None) -> Any:
    def decorator(func: Any) -> Any:
        @wraps(func)
        async def wrapper(
            *args: tuple[Any], **kwargs: dict[str, dict[str, Any]]
        ) -> Any | None:
            try:
                return await func(*args, **kwargs)
            except PyMongoError as e:
                print(f"[MongoDB Error in {func.__name__}]: {e}")
                return default

        return wrapper

    return decorator
