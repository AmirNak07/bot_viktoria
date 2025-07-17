import asyncio
from typing import Any

from httpx import AsyncClient

from scheduler.parsers.rsv_parser.config import (
    INTERNSHIPS_API,
    INTERNSHIPS_API_PARAMS,
    REGIONS_API,
)
from scheduler.parsers.rsv_parser.scraper.downloader import fetch_page_json
from scheduler.parsers.rsv_parser.scraper.parser import parse_internships


async def collect() -> list[dict[str, Any]]:
    async with AsyncClient() as session:
        tasks = [
            fetch_page_json(
                session,
                INTERNSHIPS_API,
                INTERNSHIPS_API_PARAMS,
            ),
            fetch_page_json(session, REGIONS_API),
        ]
        internships_data, regions_data = await asyncio.gather(*tasks)
        internships = internships_data["data"]
        regions = {
            region["id"]: region["field_value"] for region in regions_data["data"]
        }
        return parse_internships(internships, regions)


asyncio.run(collect())
