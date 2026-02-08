from datetime import datetime

from sqlalchemy import Column, Date, ForeignKey, Integer

from app.core.db import Base


class CustomerOrder(Base):
    __tablename__ = 'customer_order'
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    create_date = Column(Date, default=datetime.now().date(), nullable=False)
