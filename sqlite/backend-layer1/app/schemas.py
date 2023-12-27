from pydantic import BaseModel
from typing import Optional


class TransactionBase(BaseModel):
    amount: float
    description: Optional[str] = None


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int

    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    name: str


class ItemCreate(BaseModel):
    name: str


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
