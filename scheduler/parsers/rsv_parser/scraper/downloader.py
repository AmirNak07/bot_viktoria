from typing import Any

from httpx import AsyncClient


async def fetch_page_json(
    session: AsyncClient, link: str, params: dict[str, Any] | None = None
) -> Any:
    request = await session.get(link, params=params)
    request.raise_for_status()
    return request.json()
