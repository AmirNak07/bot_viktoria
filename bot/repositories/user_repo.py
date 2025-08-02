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
        is_active: bool,
    ) -> None:
        await self.collection.insert_one(
            {
                "user_id": user_id,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "is_active": is_active,
            }
        )

    async def get_all_user_ids(self) -> list[int]:
        cursor = self.collection.find({"is_active": True}, {"user_id": 1})
        user_ids = []
        async for doc in cursor:
            user_ids.append(doc["user_id"])
        return user_ids
