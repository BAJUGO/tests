from pymongo import AsyncMongoClient
from fastapi import Depends


class MongoHelper:
    def __init__(self, db_name: str, url: str = "mongodb://user:password@localhost:27017"):
        self.client = AsyncMongoClient(url)
        self.db = self.client[db_name]


    async def get_session(self):
        async with self.client.start_session() as session:
            yield session
