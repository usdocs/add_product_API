from sqlalchemy import Column, ForeignKey, Integer, String

from app.core.db import Base


class Category(Base):
    name = Column(String(100), nullable=False)
    parent_id = Column(Integer, ForeignKey('category.id'))
