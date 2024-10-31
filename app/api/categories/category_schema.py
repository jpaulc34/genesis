from pydantic import BaseModel, EmailStr
from typing import List

class CategoryCreate(BaseModel):
    name: str
    description: str

class CategoryResponse(BaseModel):
    id: str
    name: str
    description: str

    # class ConfigDict:
    #     from_attributes = True

class CategoryWithProductsResponse(BaseModel):
    id: str
    name: str
    description: str
    products: List