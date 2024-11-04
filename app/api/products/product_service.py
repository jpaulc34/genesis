from fastapi import Request
from typing import List, Optional, Dict

from app.api.categories.category_repository import CategoryRepository
from app.api.products.product_repository import ProductRepository
from app.api.products.product_schema import ProductCreate, ProductUpdate, ProductResponse
from app.api.serializers import serialize_category

class ProductService:
    def __init__(self, request: Request):
        self.product_repository = ProductRepository(request)
        self.category_repository = CategoryRepository(request)

    async def create_product(self, product_data: ProductCreate) -> str:
        return await self.product_repository.insert_one(product_data.model_dump())

    # async def get_all_products(self) -> List[ProductResponse]:
    #     return await self.product_repository.get_all_products()

    async def get_product_by_id(self, product_id: str) -> Optional[ProductResponse]:
        product = await self.product_repository.find_by_id(product_id)
        category = await self.category_repository.find_by_id(product["category_id"])
        return {
                **product,
                "category": serialize_category(category)
            }
    
    async def update_product(self, product_id: str, update_data: ProductUpdate):
        return await self.product_repository.update_one(product_id, update_data.model_dump())
    
    async def delete_product(self, product_id: str):
        return await self.product_repository.delete_one(product_id)
    
    async def get_all_products(self) -> List[ProductResponse]:
        products = await self.product_repository.find_all()
        
        # Collect unique category IDs from products
        category_ids = list({product["category_id"] for product in products})
        
        # Fetch all categories by IDs in a single query
        categories = await self.category_repository.get_categories_by_ids(category_ids)
        
        # Embed category details in each product based on `category_id`
        return [
            {
                **product,
                "category": {
                    "id": str(categories[product["category_id"]]["_id"]),
                    "name": categories[product["category_id"]]["name"],
                    "description": categories[product["category_id"]]["description"],
                } if product["category_id"] in categories else None
            }
            for product in products
        ]