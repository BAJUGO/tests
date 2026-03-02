from fastapi import FastAPI, Depends, Body
from fastapi.exceptions import HTTPException
from mongo_db.db_helper import MongoHelper
from typing import Annotated

app = FastAPI()



'''
There are lots of problems with id or _id or smth like that,
so I decided to start function names with "id" or smth for 
your attention
'''

def id_list_fixed(cursor_listed: list):
    for el in cursor_listed:
        el["_id"] = str(el["_id"])
    return cursor_listed


def id_doc_fixed(doc: dict):
    doc["_id"] = str(doc["_id"])
    return doc


'''
To create new database you HAVE to write something into it,
so, in order to create DB you have to create a collection in it
'''


@app.get("/create_new_database/")
async def create_new_collection(db_name: str, collection_name: str, delete_empty_doc: bool = True):
    try:
        new_db = MongoHelper(db_name=db_name)
        new_collection = new_db.db[collection_name]
        await new_collection.insert_one({})

        if delete_empty_doc:
            await new_collection.delete_one({})

        return {"Message": "database created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/get_all_databases")
async def get_all_databases():
    databases = await MongoHelper(db_name="task_db").client.list_database_names()
    if databases:
        return databases
    raise HTTPException(status_code=403, detail="Databases weren't found")



@app.get("/get_all_collections/{db_name}")
async def get_all_collections(db_name: str):
    collections = await MongoHelper(db_name=db_name).db.list_collection_names()
    if collections:
        return collections
    raise HTTPException(status_code=404, detail="Collections weren't found")
