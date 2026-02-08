from pydantic import BaseModel, PositiveInt


class ProductOrderGet(BaseModel):
    order_id: int
    product_id: int


class ProductOrderAdd(ProductOrderGet):
    quantity: PositiveInt


class ProductOrderDB(ProductOrderAdd):
    id: int
