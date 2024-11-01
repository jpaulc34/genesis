import os

from bson import ObjectId
from fastapi import Request
from typing import List, Dict

from app.api.repositories.base_repository import BaseRepository

class VariantRepository(BaseRepository):
    def __init__(self, request: Request):
        collection = request.app.state.mongo_client[os.environ.get("DB")][os.environ.get("VARIANT_COLLECTION")]  # MongoDB collection
        super().__init__(collection)

    async def get_variants_by_product_id(self, product_id: str) -> List[Dict]:
        documents = self.collection.find({"product_id": (product_id)})
        return [{"id": str(doc["_id"]), **doc} for doc in documents]