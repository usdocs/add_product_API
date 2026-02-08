from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_available_product_quantity,
    check_customer_order_exists,
)
from app.crud import product_order_crud
from app.schemas import ProductOrderAdd, ProductOrderDB


async def create_product_order(
    obj_in: ProductOrderAdd,
    session: AsyncSession,
) -> ProductOrderDB:
    await check_available_product_quantity(
        product_order=obj_in,
        session=session,
    )
    await check_customer_order_exists(
        order_id=obj_in.order_id,
        session=session,
    )
    return await product_order_crud.create(
        obj_in=obj_in,
        session=session,
    )


async def update_product_order(
    obj_in: ProductOrderAdd,
    product_order: ProductOrderDB,
    session: AsyncSession,
) -> ProductOrderDB:
    obj_in.quantity += product_order.quantity
    await check_available_product_quantity(
        product_order=obj_in,
        session=session,
    )
    return await product_order_crud.update(
        db_obj=product_order,
        obj_in=obj_in,
        session=session,
    )
