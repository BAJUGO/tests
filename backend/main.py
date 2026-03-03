from fastapi import FastAPI

from backend.core.lifespan import lifespan
from backend.routers.mongo_router import router as mongo_router

app = FastAPI(lifespan=lifespan)

app.include_router(mongo_router)







