from fastapi import Request
from app.services.product_service import ProductService
from app.services.category_service import CategoryService

def get_product_service(request: Request) -> ProductService:
    return ProductService(request)

def get_category_service(request: Request) -> CategoryService:
    return CategoryService(request)