from pymongo import AsyncMongoClient
from tenacity import retry, stop_after_attempt, wait_fixed

from scheduler.parsers.rosmol_parser.parser import collect


@retry(stop=stop_after_attempt(3), wait=wait_fixed(10 * 60), reraise=True)
async def parse_rosmol(collection: AsyncMongoClient, creator: str) -> None:
    items = await collect()
    await collection.delete_many({"creator": creator})

    docs = []
    for item in items:
        docs.append(
            {
                "creator": item["creator"],
                "title": item["title"],
                "place": item["place"],
                "date": item["date"],
                "category_of_participants": item["category_of_participants"],
                "link": item["link"],
            }
        )
    if docs:
        await collection.insert_many(docs)
