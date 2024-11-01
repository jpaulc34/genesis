from fastapi import Request
from typing import List, Optional, Dict

from app.api.variants.variant_repository import VariantRepository
from app.api.variants.variant_schema import VariantCreate, VariantResponse

class VariantService:
    def __init__(self, request: Request):
        self.variant_repository = VariantRepository(request)

    async def create_variant(self, product_id: str, variant_data: VariantCreate) -> str:
        variant = variant_data.model_dump()
        variant["product_id"] = product_id
        return await self.variant_repository.insert_one(variant)

    async def get_all_variants(self, product_id) -> List[VariantResponse]:
        return await self.variant_repository.find_all()

    async def get_variant_by_id(self, variant_id: str) -> Optional[VariantResponse]:
        return await self.variant_repository.find_by_id(variant_id)
    
    async def update_variant(self, variant_id: str, update_data: Dict):
        return await self.variant_repository.update_one(variant_id, update_data)
    
    async def delete_variant(self, product_id: str, variant_id: str):
        variants = await self.get_variants_by_product_id(product_id)
        variant_ids = [variant["id"] for variant in variants]
        if variant_id in variant_ids:
            return await self.variant_repository.delete_one(variant_id)
        
    async def get_variants_by_product_id(self, product_id: str) -> List[VariantResponse]:
        return await self.variant_repository.get_variants_by_product_id(product_id)