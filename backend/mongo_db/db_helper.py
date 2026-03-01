from pymongo import AsyncMongoClient
from fastapi import Depends


class MongoHelper:
    def __init__(self, url: str, db_name: str):
        self.client = AsyncMongoClient(url)
        self.db = self.client[db_name]

    def get_collection(self, name: str):
        return self.db[name]

    async def get_session(self):
        async with self.client.start_session() as session:
            yield session


test_db = MongoHelper(
    url="mongodb://user:password@localhost:27017",
    db_name="test"
)

ses_dep = Depends(test_db.get_session)
