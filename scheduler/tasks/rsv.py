from tenacity import retry, stop_after_attempt, wait_fixed

from scheduler.database.models.rsv import RSVEventModel
from scheduler.parsers.rsv_parser.parser import collect


@retry(stop=stop_after_attempt(3), wait=wait_fixed(10 * 60), reraise=True)
async def parser_rsv() -> None:
    data = await collect()
    documents = [RSVEventModel(**item) for item in data]

    await RSVEventModel.find(RSVEventModel.creator == "rsv").delete()

    for doc in documents:
        await doc.insert()
