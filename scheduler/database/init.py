from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from scheduler.config import settings
from scheduler.database.models.rosmol import RosmolEventModel
from scheduler.database.models.rsv import RSVEventModel
from scheduler.database.models.vk import VKEventModel


async def init_db() -> None:
    client: AsyncIOMotorClient = AsyncIOMotorClient(settings.MONGO_URI)  # type: ignore
    await init_beanie(
        database=client.get_default_database(),
        document_models=[VKEventModel, RosmolEventModel, RSVEventModel],
    )
