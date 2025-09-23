from typing import Optional
from pydantic import BaseModel,Field

class Item(BaseModel):
    id: int
    name: str= Field(
    ...,
    min_length=3,
    max_length=10,
    pattern=r'^[a-zA-Z0-9]+$',
    title='Username',
    description='must be alpha-numeric',
    example='johndoe777'
)

    description: Optional[str] = None
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str


class ResponseModel(BaseModel):
    success: bool
    message: str
    data: ItemResponse
