import os

from fastapi import Request
from typing import List, Dict

from app.api.repositories.base_repository import BaseRepository

class ProductRepository(BaseRepository):
    def __init__(self, request: Request):
        collection = request.app.state.mongo_client[os.environ.get("DB")][os.environ.get("PRODUCT_COLLECTION")]  # MongoDB collection
        super().__init__(collection)
    
    async def get_products_by_category_id(self, category_id: str) -> Dict:
        products = self.collection.find({"category_id": (category_id)})
        return [{"id": str(product["_id"]), **product} for product in products]