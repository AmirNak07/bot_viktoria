from typing import Any

from httpx import AsyncClient


async def fetch_page(
    session: AsyncClient, link: str, params: dict[str, Any] | None = None
) -> str:
    request = await session.get(link, params=params)
    request.raise_for_status()
    return request.text
