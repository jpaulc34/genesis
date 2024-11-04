from fastapi import Request

from app.api.categories.category_service import CategoryService
from app.api.inventories.inventory_service import InventoryService
from app.api.products.product_service import ProductService
from app.api.variants.variant_service import VariantService

def get_category_service(request: Request) -> CategoryService:
    return CategoryService(request)

def get_product_service(request: Request) -> ProductService:
    return ProductService(request)

def get_variant_service(request: Request) -> VariantService:
    return VariantService(request)

def get_inventory_service(request: Request) -> InventoryService:
    return InventoryService(request)