from fastapi import APIRouter, Request, Depends
from typing import List, Dict

from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter(
        prefix="/products",
        tags= ["Products"],
        # dependencies= [Depends(validate_token)]
    )

def get_product_service(request: Request) -> ProductService:
    return ProductService(request)

@router.get("/")
async def list_products(service: ProductService = Depends(get_product_service)) -> List[ProductResponse]:
    return await service.get_all_products()

@router.post("/")
async def create_product(product_data: ProductCreate, service: ProductService = Depends(get_product_service)):
    return await service.create_product(product_data)

@router.get("/{id}")
async def get_product( id: str, service: ProductService = Depends(get_product_service)) -> ProductResponse:
    return await service.get_product_by_id(id)

@router.put("/{product_id}")
async def update_product( product_id: str, product_data: Dict, service: ProductService = Depends(get_product_service)) -> ProductResponse:
    return await service.update_product(product_id, product_data)

@router.delete("/{product_id}")
async def list_products(product_id: str, service: ProductService = Depends(get_product_service)):
    return await service.delete_product(product_id)