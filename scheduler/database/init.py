from beanie import init_beanie
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient

from database.models.vk import VKEventModel


async def init_db() -> None:
    client: AsyncIOMotorClient = AsyncIOMotorClient(settings.MONGO_URI)  # type: ignore
    await init_beanie(
        database=client.get_default_database(), document_models=[VKEventModel]
    )
