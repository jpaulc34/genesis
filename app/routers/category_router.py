from fastapi import APIRouter, Request, Depends
from typing import List, Dict

from app.schemas.category_schema import CategoryCreate, CategoryResponse, CategoryWithProductsResponse
from app.services.category_service import CategoryService

router = APIRouter(
        prefix="/categories",
        tags= ["Categories"],
        # dependencies= [Depends(validate_token)]
    )

def get_category_service(request: Request) -> CategoryService:
    return CategoryService(request)

@router.get("/")
async def list_categories(service: CategoryService = Depends(get_category_service)) -> List[CategoryResponse]:
    return await service.get_all_categories()

@router.post("/")
async def create_category(category_data: CategoryCreate, service: CategoryService = Depends(get_category_service)):
    return await service.create_category(category_data)

@router.get("/{id}")
async def get_category( id: str, service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return await service.get_category_by_id(id)

@router.get("/{id}/products")
async def get_products_by_category_id( id: str, service: CategoryService = Depends(get_category_service)) -> CategoryWithProductsResponse:
    return await service.get_products_by_category_id(id)

@router.put("/{id}")
async def update_category( id: str, category_data: Dict, service: CategoryService = Depends(get_category_service)) -> CategoryResponse:
    return await service.update_category(id, category_data)

@router.delete("/{id}")
async def list_category(id: str, service: CategoryService = Depends(get_category_service)):
    return await service.delete_category(id)