import os

from fastapi import FastAPI
from pymongo import MongoClient
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo_client = MongoClient(os.environ.get("MONGO_URI"))
    app.state.mongo_client = mongo_client
    yield
    mongo_client.close()