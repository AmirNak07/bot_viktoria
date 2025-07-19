from tenacity import retry, stop_after_attempt, wait_fixed

from scheduler.database.models.vk import VKEventModel
from scheduler.parsers.vk_parser.parser import collect


@retry(stop=stop_after_attempt(3), wait=wait_fixed(10 * 60), reraise=True)
async def parse_vk() -> None:
    data = await collect()
    documents = [VKEventModel(**item) for item in data]

    await VKEventModel.find(VKEventModel.creator == "vk").delete()

    for doc in documents:
        await doc.insert()
