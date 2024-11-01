from pydantic import BaseModel, EmailStr
from typing import List

class VariantCreate(BaseModel):
    name: str
    description: str
    sku: str
    quantity: int
    cost_price: float
    selling_price: float

class VariantResponse(BaseModel):
    id: str
    name: str
    description: str
    sku: str
    quantity: int
    cost_price: float
    selling_price: float
    product_id: str