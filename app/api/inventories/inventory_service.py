from fastapi import Request
from typing import List, Optional, Dict

from app.api.inventories.inventory_repository import InventoryRepository
from app.api.inventories.inventory_schema import InventoryUpdate

from app.api.serializers import serialize_category

class InventoryService:
    def __init__(self, request: Request):
        self.inventory_repository = InventoryRepository(request)

    async def get_stock(self, product_id: str) -> Optional[InventoryUpdate]:
        return await self.inventory_repository.get_stock(product_id)
        
    async def update_stock(self, product_id: str, update_data: InventoryUpdate):
        return await self.inventory_repository.update_stock(product_id, update_data.model_dump())