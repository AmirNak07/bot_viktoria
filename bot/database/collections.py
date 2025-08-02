from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from bot.database.mongodb import MongoDB


class MongoCollections:
    def __init__(self, mongo: MongoDB):
        self.users: AsyncCollection[Any] = mongo.get_collection("users")
        self.events: AsyncCollection[Any] = mongo.get_collection("events")
