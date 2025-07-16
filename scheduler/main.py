import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler  # type: ignore

from scheduler.tasks.rosmol import parse_rosmol
from scheduler.tasks.vk import parse_vk


async def main() -> None:
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        parse_vk,
        trigger="interval",
        hours=3,
        id="vk_parser_job",
        max_instances=1,
    )

    scheduler.add_job(
        parse_rosmol,
        trigger="interval",
        hours=3,
        id="rosmol_parser_job",
        max_instances=1,
    )

    scheduler.start()
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
