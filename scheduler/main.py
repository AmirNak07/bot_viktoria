import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler  # type: ignore

from scheduler.tasks import parse_rosmol, parse_vk, parser_rsv


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

    scheduler.add_job(
        parser_rsv,
        trigger="interval",
        hours=3,
        id="rsv_parser_job",
        max_instances=1,
    )

    scheduler.start()
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
