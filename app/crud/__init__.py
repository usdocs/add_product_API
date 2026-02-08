from .product_order import product_order_crud # noqa

from app.crud.base import CRUDBase
from app.models import CustomerOrder, Product

product_crud = CRUDBase(Product)
customer_order_crud = CRUDBase(CustomerOrder)
