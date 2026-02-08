from sqlalchemy import Column, String

from app.core.db import Base


class Customer(Base):
    name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
