from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import ProductOrder
from app.schemas import ProductOrderGet


class CRUDProductOrder(CRUDBase):
    async def get_by_product_and_order(
        self,
        session: AsyncSession,
        obj_data: ProductOrderGet,
    ) -> ProductOrder:
        db_obj = await session.execute(
            select(ProductOrder).where(
                ProductOrder.product_id == obj_data.product_id,
                ProductOrder.order_id == obj_data.order_id
            )
        )
        return db_obj.scalars().first()


product_order_crud = CRUDProductOrder(ProductOrder)
