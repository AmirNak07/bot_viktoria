from typing import Any

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection


class MongoDB:
    def __init__(self, connection_uri: str, db_name: str):
        self._client: AsyncMongoClient[Any] = AsyncMongoClient(connection_uri)
        self._db = self._client[db_name]

    def get_collection(self, name: str) -> AsyncCollection[Any]:
        return self._db[name]

    async def close(self) -> None:
        await self._client.close()
