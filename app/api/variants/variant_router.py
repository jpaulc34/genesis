from fastapi import APIRouter, Request, Depends, HTTPException, status
from typing import List, Dict

from app.dependencies.service_dependency import get_variant_service
from app.api.variants.variant_schema import VariantCreate, VariantResponse
from app.api.variants.variant_service import VariantService

router = APIRouter(
        # prefix="/",
        tags= ["Variants"],
        dependencies= [Depends(get_variant_service)]
    )

@router.get("/products/{product_id}/variants", response_model=List[VariantResponse])
async def list_variants(product_id: str, service: VariantService = Depends()):
    return await service.get_variants_by_product_id(product_id)

@router.post("/products/{product_id}/variants")
async def create_variant(variant_data: VariantCreate, product_id: str, service: VariantService = Depends()):
    return await service.create_variant(product_id, variant_data)

@router.get("/variants/{variant_id}", response_model=VariantResponse)
async def get_variant( variant_id: str, service: VariantService = Depends()):
    variant = await service.get_variant_by_id(variant_id)
    if not variant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Variant not found")
    return variant

@router.put("/variants/{variant_id}")
async def update_variant( variant_id: str, variant_data: Dict, service: VariantService = Depends()):
    updated = await service.update_variant(variant_id, variant_data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Variant not found")
    return updated

@router.delete("/products/{product_id}/variants/{variant_id}")
async def delete_variant(product_id: str, variant_id: str, service: VariantService = Depends()):
    success = await service.delete_variant(product_id, variant_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return {"status": "deleted", "id": variant_id}