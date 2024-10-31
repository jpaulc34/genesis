import os

from bson import ObjectId
from fastapi import Request
from pymongo.collection import Collection
from typing import List, Dict

from app.api.repositories.base_repository import BaseRepository
    
class UserRepository(BaseRepository):
    def __init__(self, request: Request):
        collection = request.app.state.mongo_client[os.environ.get("DB")][os.environ.get("USER_COLLECTION")]  # MongoDB collection
        super().__init__(collection)