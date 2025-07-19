import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler  # type: ignore
from pymongo import AsyncMongoClient

from scheduler.config import settings
from scheduler.tasks import parse_rosmol, parse_vk, parser_rsv


async def main() -> None:
    client = AsyncMongoClient(settings.MONGO_URI)
    db = client.mydatabase
    collection = db.events

    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        parse_vk,
        kwargs={"collection": collection, "creator": "vk"},
        trigger="interval",
        hours=3,
        id="vk_parser_job",
    )

    scheduler.add_job(
        parse_rosmol,
        kwargs={"collection": collection, "creator": "rosmol"},
        trigger="interval",
        hours=3,
        id="rosmol_parser_job",
    )

    scheduler.add_job(
        parser_rsv,
        kwargs={"collection": collection, "creator": "rsv"},
        trigger="interval",
        hours=3,
        id="rsv_parser_job",
    )

    scheduler.start()
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
