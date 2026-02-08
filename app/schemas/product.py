from pydantic import BaseModel, PositiveInt


class ProductDB(BaseModel):
    id: int
    name: str
    category_id: int
    quantity: PositiveInt
    price: float
