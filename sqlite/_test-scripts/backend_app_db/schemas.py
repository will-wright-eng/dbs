import typing as t

from pydantic import BaseModel


class UserBase(BaseModel):
    fp_hash: str

    class Config:
        orm_mode = True


class UserOut(UserBase):
    pass


class UserCreate(UserBase):
    email: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class ProductDetails(BaseModel):
    roastery_name: t.Optional[str] = None
    roastery_location: t.Optional[str] = None
    cultivar_name: t.Optional[str] = None
    cultivar_origin: t.Optional[str] = None
    farm_name: t.Optional[str] = None
    farm_region: t.Optional[str] = None
    farm_elevation: t.Optional[str] = None
    brand_name: t.Optional[str] = None


class InsertEntry(UserBase, ProductDetails):
    grind_setting: float
    bean_weight: float
    water_temperature: t.Optional[float] = None
    extraction_time: t.Optional[float] = None
    extraction_weight: t.Optional[float] = None
    extraction_notes: t.Optional[str] = None


# class UserEdit(UserBase):
#     password: t.Optional[str] = None

#     class Config:
#         orm_mode = True


# class User(UserBase):
#     id: int

#     class Config:
#         orm_mode = True


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     email: str = None
#     permissions: str = "user"
