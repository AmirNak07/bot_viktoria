from tenacity import retry, stop_after_attempt, wait_fixed

from scheduler.database.models.rosmol import RosmolEventModel
from scheduler.parsers.rosmol_parser.parser import collect


@retry(stop=stop_after_attempt(3), wait=wait_fixed(10 * 60), reraise=True)
async def parse_rosmol() -> None:
    data = await collect()
    documents = [RosmolEventModel(**item) for item in data]

    await RosmolEventModel.find(RosmolEventModel.creator == "rosmol").delete()

    for doc in documents:
        await doc.insert()
