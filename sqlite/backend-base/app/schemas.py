from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str


class ItemCreate(BaseModel):
    name: str


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
