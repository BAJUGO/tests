from typing import Annotated

from ..crud import mongo_crud

from fastapi import APIRouter, HTTPException, Body, Depends

from ..core.lifespan import get_mongo
from ..mongo_db.mongo_helper import MongoHelper

router = APIRouter(prefix="/mongo")

mongo_dep: MongoHelper = Depends(get_mongo)


@router.get("/get_all_databases")
async def get_all_databases(
                            mongo=mongo_dep):
    databases = await mongo.client.list_database_names()
    if databases:
        return databases
    raise HTTPException(status_code=403, detail="Databases weren't found")


@router.get("/get_all_collections/{db_name}")
async def get_all_collections(db_name: str,
                              mongo=mongo_dep):
    db = mongo.client[db_name]
    collections = await db.list_collection_names()
    if collections:
        return collections
    raise HTTPException(status_code=404, detail="Collections weren't found")


@router.get("/get_all_docs/{db_name}/{collection_name}")
async def get_all_docs(db_name: str, collection_name: str,
                       mongo=mongo_dep):
    db = mongo.client[db_name]
    collection = db[collection_name]
    cursor = await collection.find().to_list()
    if cursor:
        return mongo_crud.id_list_fixed(cursor)
    raise HTTPException(status_code=404, detail="Collections weren't found")


@router.post("/create_new_database/")
async def create_new_database(db_name: str, collection_name: str, delete_empty_doc: bool = True,
                              mongo=mongo_dep):
    try:
        new_db = mongo.client[db_name]
        new_collection = new_db[collection_name]
        await new_collection.insert_one({})

        if delete_empty_doc:
            await new_collection.delete_one({})

        return {"Message": "database created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/create_new_document/{db_name}/{collection_name}")
async def create_new_document(db_name: str, collection_name: str,
                              document: Annotated[dict, Body(examples=[{"first_key": "first_value", "second_key": "second_value"}])],
                              mongo=mongo_dep):
    db = mongo.client[db_name]
    collection = db[collection_name]
    await collection.insert_one(document)
    return {"Message": "document created successfully"}


@router.delete("/delete_collection/{db_name}/{collection_name}")
async def delete_collection(db_name: str, collection_name: str,
                          mongo=mongo_dep):
    try:
        await mongo.client[db_name][collection_name].drop()
        return {"Message": "database deleted successfully"}
    except Exception as e:
        raise (HTTPException(status_code=400, detail=str(e)))


@router.delete("/delete_database/{db_name}")
async def delete_database(db_name: str,
                          mongo=mongo_dep):
    try:
        await mongo.client.drop_database(db_name)
        return {"Message": "database deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
