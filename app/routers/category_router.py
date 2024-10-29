from fastapi import APIRouter, Request, Depends, HTTPException, status
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

@router.get("/", response_model=List[CategoryResponse])
async def list_categories(service: CategoryService = Depends(get_category_service)):
    return await service.get_all_categories()

@router.post("/", response_model=CategoryResponse)
async def create_category(category_data: CategoryCreate, service: CategoryService = Depends(get_category_service)):
    return await service.create_category(category_data)

@router.get("/{id}",response_model=CategoryResponse)
async def get_category( id: str, service: CategoryService = Depends(get_category_service)):
    category = await service.get_category_by_id(id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category

@router.get("/{id}/products", response_model=CategoryWithProductsResponse)
async def get_products_by_category_id( id: str, service: CategoryService = Depends(get_category_service)):
    return await service.get_products_by_category_id(id)

@router.put("/{id}", response_model=CategoryResponse)
async def update_category( id: str, category_data: Dict, service: CategoryService = Depends(get_category_service)):
    updated = await service.update_category(id, category_data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return updated

@router.delete("/{id}")
async def delete_category(id: str, service: CategoryService = Depends(get_category_service)):
    success = await service.delete_category(id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return {"status": "deleted", "id": id}
