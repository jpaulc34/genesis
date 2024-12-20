from fastapi import Request
from typing import List, Optional, Dict

from app.api.categories.category_repository import CategoryRepository
from app.api.categories.category_schema import CategoryCreate, CategoryResponse, CategoryWithProductsResponse
from app.api.products.product_repository import ProductRepository
from app.api.serializers import serialize_product

class CategoryService:
    def __init__(self, request: Request):
        self.product_repository = ProductRepository(request)
        self.category_repository = CategoryRepository(request)

    async def create_category(self, category_data: CategoryCreate) -> str:
        return await self.category_repository.insert_one(category_data.model_dump())

    async def get_all_categories(self) -> List[CategoryResponse]:
        return await self.category_repository.find_all()

    async def get_category_by_id(self, category_id: str) -> Optional[CategoryResponse]:
        return await self.category_repository.find_by_id(category_id)
    
    async def update_category(self, category_id: str, update_data: Dict) -> CategoryResponse:
        return await self.category_repository.update_one(category_id, update_data)
    
    async def delete_category(self, category_id: str):
        return await self.category_repository.delete_one(category_id)
    
    async def get_products_by_category_id(self, category_id: str) -> Optional[CategoryWithProductsResponse]:
        category = await self.category_repository.find_by_id(category_id)
        products = await self.product_repository.get_products_by_category_id(category_id)

        category["products"] = serialize_product(products)
        return category