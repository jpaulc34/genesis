from fastapi import Request
from app.api.products.product_service import ProductService
from app.api.categories.category_service import CategoryService

def get_product_service(request: Request) -> ProductService:
    return ProductService(request)

def get_category_service(request: Request) -> CategoryService:
    return CategoryService(request)