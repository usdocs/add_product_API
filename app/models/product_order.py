from sqlalchemy import Column, ForeignKey, Integer

from app.core.db import Base


class ProductOrder(Base):
    __tablename__ = 'product_order'
    order_id = Column(Integer, ForeignKey('customer_order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
