from fastapi import APIRouter, HTTPException
from ..mongo_db.db_helper import MongoHelper


router = APIRouter(prefix="/mongo")


@router.get("/create_new_database/")
async def create_new_database(db_name: str, collection_name: str, delete_empty_doc: bool = True):
    try:
        new_db = MongoHelper(db_name=db_name)
        new_collection = new_db.db[collection_name]
        await new_collection.insert_one({})

        if delete_empty_doc:
            await new_collection.delete_one({})

        return {"Message": "database created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get_all_databases")
async def get_all_databases():
    databases = await MongoHelper(db_name="task_db").client.list_database_names()
    if databases:
        return databases
    raise HTTPException(status_code=403, detail="Databases weren't found")



@router.get("/get_all_collections/{db_name}")
async def get_all_collections(db_name: str):
    collections = await MongoHelper(db_name=db_name).db.list_collection_names()
    if collections:
        return collections
    raise HTTPException(status_code=404, detail="Collections weren't found")