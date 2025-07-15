from database.init import init_db
from database.models.vk import VKEventModel
from parsers.vk_parser.parser import collect
from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(3), wait=wait_fixed(10), reraise=True)
async def parse_vk() -> None:
    await init_db()
    data = await collect()
    documents = [VKEventModel(**item) for item in data]

    await VKEventModel.find(VKEventModel.creator == "vk").delete()

    for doc in documents:
        await doc.insert()
