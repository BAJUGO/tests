from fastapi import FastAPI, Depends
import pymongo
from mongo_db.db_helper import test_db, ses_dep
import pprint


app = FastAPI()

@app.get("/")
async def root(session = Depends(test_db.get_session)):
    collection = test_db.get_collection("test_users")
    return await collection.find_one()
    pprint.pprint(await collection.find_one())
