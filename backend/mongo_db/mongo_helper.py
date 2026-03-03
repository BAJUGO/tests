from pymongo import AsyncMongoClient
from fastapi import Depends


class MongoHelper:
    def __init__(self, url: str):
        self.client = AsyncMongoClient(url)

    async def get_session(self):
        async with self.client.start_session() as session:
            yield session

    def get_db(self, db_name):
        return self.client[db_name]

    def get_collection(self, db_name, collection_name):
        return self.client[db_name][collection_name] if self.client[db_name][collection_name] else None

    async def close(self):
        await self.client.close()


