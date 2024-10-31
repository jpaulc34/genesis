from fastapi import APIRouter, Request, Depends, HTTPException, status
from typing import List, Dict

from app.dependencies.service_dependency import get_product_service
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter(
        prefix="/products",
        tags= ["Products"],
        dependencies= [Depends(get_product_service)]
    )

@router.get("/", response_model=List[ProductResponse])
async def list_products(service: ProductService = Depends()):
    return await service.get_all_products()

@router.post("/")
async def create_product(product_data: ProductCreate, service: ProductService = Depends()):
    return await service.create_product(product_data)

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product( product_id: str, service: ProductService = Depends()):
    product = await service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return product

@router.put("/{product_id}")
async def update_product( product_id: str, product_data: Dict, service: ProductService = Depends()):
    updated = await service.update_product(product_id, product_data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return updated

@router.delete("/{product_id}")
async def delete_product(product_id: str, service: ProductService = Depends()):
    success = await service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return {"status": "deleted", "id": product_id}