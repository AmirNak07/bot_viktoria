from typing import Any

from bot.repositories.event_repo import EventsRepository
from bot.services.interfaces import IEventsService
from bot.utils.decorators import handle_mongo_errors
from bot.utils.field_labels import format_event


class EventsService(IEventsService):
    def __init__(self, repo: EventsRepository):
        self.repo = repo

    @handle_mongo_errors(default=[])  # type: ignore
    async def get_all(self) -> list[dict[str, Any]]:
        documets = await self.repo.get_all()
        for i in range(len(documets)):
            del documets[i]["_id"]
        result = []
        for doc in documets:
            result.append(format_event(doc))

        return result

    @handle_mongo_errors(default=[])  # type: ignore
    async def get_by_creator(self, creator: str) -> list[dict[str, Any]]:
        documets = await self.repo.get_by_creator(creator)
        for i in range(len(documets)):
            del documets[i]["_id"]
        result = []
        for doc in documets:
            result.append(format_event(doc))
        return result

    @handle_mongo_errors(default=[])  # type: ignore
    async def get_creators(self) -> list[str]:
        results = await self.repo.get_creators()
        return results
