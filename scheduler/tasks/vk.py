from pymongo import AsyncMongoClient
from tenacity import retry, stop_after_attempt, wait_fixed

from scheduler.parsers.vk_parser.parser import collect


@retry(stop=stop_after_attempt(3), wait=wait_fixed(10 * 60), reraise=True)
async def parse_vk(collection: AsyncMongoClient, creator: str) -> None:
    items = await collect()
    await collection.delete_many({"creator": creator})

    docs = []
    for item in items:
        docs.append(
            {
                "creator": item["creator"],
                "title": item["title"],
                "team": item["team"],
                "city": item["city"],
                "format_of_work": item["format_of_work"],
                "employment": item["employment"],
                "tasks": item["tasks"],
                "need_to_have": item["need_to_have"],
                "link": item["link"],
                "type_of_work": item["type_of_work"],
                "direction": item["direction"],
            }
        )
    if docs:
        await collection.insert_many(docs)
