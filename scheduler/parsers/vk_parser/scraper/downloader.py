import asyncio

from httpx import AsyncClient, HTTPError


async def fetch_page(link: str, session: AsyncClient) -> str:
    """Loads a web page asynchronously"""
    response = await session.get(link)
    response.raise_for_status()
    return response.text


async def fetch_multiple_pages(links: list[str]) -> list[str]:
    """Parallel loading of multiple pages"""
    async with AsyncClient() as session:
        tasks = [fetch_page(link, session) for link in links]
        try:
            result = await asyncio.gather(*tasks)
        except HTTPError as e:
            raise RuntimeError(f"Ошибка при загрузке страниц: {e}") from None
    return result
