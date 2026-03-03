from fastapi import FastAPI
from routers.mongo_router import router as mongo_router

app = FastAPI()

app.include_router(mongo_router)







