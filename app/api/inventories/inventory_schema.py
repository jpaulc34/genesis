from pydantic import BaseModel, EmailStr, PositiveInt
from typing import List

class InventoryUpdate(BaseModel):
    quantity: PositiveInt