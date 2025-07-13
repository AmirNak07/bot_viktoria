import asyncio

from database.init import init_db
from database.models.vk import VKEventModel
from parsers.vk_parser.parser import collect


async def main() -> None:
    await init_db()
    data = await collect()
    documents = [VKEventModel(**item) for item in data]

    await VKEventModel.find(VKEventModel.creator == "vk").delete()

    for doc in documents:
        await doc.insert()


asyncio.run(main())
