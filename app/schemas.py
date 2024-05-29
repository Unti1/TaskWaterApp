from pydantic import BaseModel
from typing import List

class ItemReport(BaseModel):
    item_id: str
    quantity: int

class StoreReport(BaseModel):
    store_id: str
    report: List[ItemReport]

class Operation(BaseModel):
    operation: str  # 'demand' or 'supply'
    item_id: str
    quantity: int

class GroupOperation(BaseModel):
    operation: str  # 'demand' or 'supply'
    items: List[ItemReport]
