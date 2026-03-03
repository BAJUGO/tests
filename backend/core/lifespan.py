from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from ..mongo_db.mongo_helper import MongoHelper


@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo = MongoHelper(url="mongodb://user:password@localhost:27017")
    app.state.mongo = mongo
    try:
        yield
    finally:
        await mongo.close()


async def get_mongo(request: Request) -> MongoHelper:
    return request.app.state.mongo