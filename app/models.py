from pydantic import BaseModel, Field
from typing import Literal


Status = Literal["completed", "pending", "canceled"]
Criterion = Literal[Status, "all"]


class Order(BaseModel):
    id: int
    item: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., ge=0)
    status: Status


class Json(BaseModel):
    orders: list[Order]
    criterion: Criterion