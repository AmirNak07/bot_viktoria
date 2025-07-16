import asyncio
from typing import Any

from httpx import AsyncClient

from scheduler.parsers.rosmol_parser.config import (
    ROSMOL_FORUMS_PARAM,
    ROSMOL_FORUMS_PATH,
    ROSMOL_FORUMS_URL,
)
from scheduler.parsers.rosmol_parser.scraper.downloader import fetch_page
from scheduler.parsers.rosmol_parser.scraper.parser import get_forum_links, parse_html


async def collect() -> list[dict[str, Any]]:
    async with AsyncClient() as session:
        main_page_url = f"{ROSMOL_FORUMS_URL}/{ROSMOL_FORUMS_PATH}"
        html = await fetch_page(session, main_page_url, ROSMOL_FORUMS_PARAM)

        forum_links = get_forum_links(html)

        tasks = [fetch_page(session, ROSMOL_FORUMS_URL + link) for link in forum_links]
        forums_html = await asyncio.gather(*tasks)

    return parse_html(forums_html)
