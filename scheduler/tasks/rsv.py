from pymongo import AsyncMongoClient
from tenacity import retry, stop_after_attempt, wait_fixed

from scheduler.parsers.rsv_parser.parser import collect


@retry(stop=stop_after_attempt(3), wait=wait_fixed(10 * 60), reraise=True)
async def parser_rsv(collection: AsyncMongoClient, creator: str) -> None:
    items = await collect()
    await collection.delete_many({"creator": creator})

    docs = []
    for item in items:
        docs.append(
            {
                "creator": item["creator"],
                "title": item["title"],
                "institute_name": item["institute_name"],
                "regions": item["regions"],
                "industry_name": item["industry_name"],
                "skills": item["skills"],
                "duration": item["duration"],
                "work_format": item["work_format"],
                "payment": item["payment"],
                "link": item["link"],
            }
        )
    if docs:
        await collection.insert_many(docs)
