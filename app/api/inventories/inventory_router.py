from fastapi import APIRouter, Request, Depends, HTTPException, status
from typing import List, Dict

from app.dependencies.service_dependency import get_product_service
from app.api.inventories.inventory_schema import InventoryUpdate
# from app.api.products.product_service import ProductService
from app.api.inventories.inventory_service import InventoryService

router = APIRouter(
        prefix="/products",
        tags= ["Inventory"],
        dependencies= [Depends(get_product_service)]
    )

@router.get("/{product_id}/stock")
async def get_product_stock( product_id: str, service: InventoryService = Depends()):
    product = await service.get_stock(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.put("/{product_id}/stock")
async def update_product_stock( product_id: str, inventory_data: InventoryUpdate, service: InventoryService = Depends()):
    updated = await service.update_stock(product_id, inventory_data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return updated