from pydantic import BaseModel, Field
from typing import Literal


Status = Literal["completed", "pending", "canceled"]
Criterion = Literal[Status, "all"]


class Order(BaseModel):
    id: int = Field(
        ...,
        description = "An integer representing the order ID",
        ge=0
    )
    item: str = Field(
        ...,
        description = "A string representing the item name", 
        min_length=1
    )
    quantity: int = Field(
        ...,
        description = "An integer representing the number of items in the order", 
        gt=0
    )
    price: float = Field(
        ...,
        description = "A number representing the price per item",
        ge=0
    )
    status: Status = Field(
        description = "A string representing the order status"
    )


class Json(BaseModel):
    orders: list[Order] = Field(
        ...,
        description = "List of orders"
    )
    criterion: Criterion = Field(
        ...,
        description = "A string that indicates the filter to be applied to the orders"
    )