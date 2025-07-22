from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from bot.repositories.interfaces import IEventsRepository


class EventsRepository(IEventsRepository):
    def __init__(self, collection: AsyncCollection[dict[str, Any]]):
        self.collection = collection

    async def get_all(self) -> list[dict[str, Any]]:
        return await self.collection.find().to_list()

    async def get_by_creator(self, creator: str) -> list[dict[str, Any]]:
        return await self.collection.find({"creator": creator}).to_list()

    async def get_creators(self) -> list[str]:
        return await self.collection.distinct("creator")
