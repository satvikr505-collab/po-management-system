from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    product_id: int
    quantity: int
    price: float


class PurchaseOrderCreate(BaseModel):
    vendor_id: int
    items: List[Item] 