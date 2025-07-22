from typing import Any

from bot.repositories.user_repo import UsersRepository
from bot.services.interfaces import IUsersService


class UsersService(IUsersService):
    def __init__(self, repo: UsersRepository):
        self.repo = repo

    async def find_user(self, user_id: int) -> dict[str, Any] | None:
        result = await self.repo.find_user(user_id)
        return result

    async def insert_user(
        self,
        user_id: int,
        username: str | None,
        first_name: str,
        last_name: str | None,
        is_new: bool,
    ) -> None:
        await self.repo.insert_user(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_new=is_new,
        )
