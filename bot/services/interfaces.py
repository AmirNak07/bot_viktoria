from typing import Any, Protocol


class IEventsService(Protocol):
    async def get_all(self) -> list[dict[str, Any]]: ...
    async def get_by_creator(self, creator: str) -> list[dict[str, Any]]: ...
    async def get_creators(self) -> list[str]: ...


class IUsersService(Protocol):
    async def find_user(self, user_id: int) -> dict[str, Any] | None: ...
    async def insert_user(
        self,
        user_id: int,
        username: str | None,
        first_name: str,
        last_name: str | None,
        is_new: bool,
    ) -> None: ...
