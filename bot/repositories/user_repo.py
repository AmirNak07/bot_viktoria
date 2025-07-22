from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from bot.repositories.interfaces import IUsersRepository


class UsersRepository(IUsersRepository):
    def __init__(self, collection: AsyncCollection[dict[str, Any]]):
        self.collection = collection

    async def find_user(self, user_id: int) -> dict[str, Any] | None:
        result = await self.collection.find_one({"user_id": user_id})
        return result

    async def insert_user(
        self,
        user_id: int,
        username: str | None,
        first_name: str,
        last_name: str | None,
        is_new: bool,
    ) -> None:
        await self.collection.insert_one(
            {
                "user_id": user_id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "is_new": is_new,
            }
        )
