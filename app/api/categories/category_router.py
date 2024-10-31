from fastapi import APIRouter, Request, Depends, HTTPException, status
from typing import List, Dict

from app.dependencies.service_dependency import get_category_service
from app.api.categories.category_schema import CategoryCreate, CategoryResponse, CategoryWithProductsResponse
from app.api.categories.category_service import CategoryService

router = APIRouter(
        prefix="/categories",
        tags= ["Categories"],
        dependencies= [Depends(get_category_service)]
    )

@router.get("/", response_model=List[CategoryResponse])
async def list_categories(service: CategoryService = Depends()):
    return await service.get_all_categories()

@router.post("/")
async def create_category(category_data: CategoryCreate, service: CategoryService = Depends()):
    return await service.create_category(category_data)

@router.get("/{id}",response_model=CategoryResponse)
async def get_category( id: str, service: CategoryService = Depends()):
    category = await service.get_category_by_id(id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category

@router.get("/{id}/products", response_model=CategoryWithProductsResponse)
async def get_products_by_category_id( id: str, service: CategoryService = Depends()):
    return await service.get_products_by_category_id(id)

@router.put("/{id}", response_model=CategoryResponse)
async def update_category( id: str, category_data: Dict, service: CategoryService = Depends()):
    updated = await service.update_category(id, category_data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return updated

@router.delete("/{id}")
async def delete_category(id: str, service: CategoryService = Depends()):
    success = await service.delete_category(id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return {"status": "deleted", "id": id}
