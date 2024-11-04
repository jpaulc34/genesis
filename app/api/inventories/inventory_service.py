from fastapi import Request
from typing import List, Optional, Dict

from app.api.categories.category_repository import CategoryRepository
from app.api.inventories.inventory_schema import InventoryUpdate
from app.api.products.product_repository import ProductRepository
from app.api.products.product_schema import ProductCreate, ProductUpdate, ProductResponse
from app.api.serializers import serialize_category

class InventoryService:
    def __init__(self, request: Request):
        self.product_repository = ProductRepository(request)

    async def get_stock(self, product_id: str) -> Optional[ProductResponse]:
        return await self.product_repository.get_stock(product_id)
        
    async def update_stock(self, product_id: str, update_data: InventoryUpdate):
        return await self.product_repository.update_stock(product_id, update_data.model_dump())