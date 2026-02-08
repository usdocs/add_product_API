from sqlalchemy import Column, Float, ForeignKey, Integer, String

from app.core.db import Base


class Product(Base):
    name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
