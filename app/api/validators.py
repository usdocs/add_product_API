from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import customer_order_crud, product_crud
from app.schemas import ProductDB, ProductOrderAdd


async def check_product_exists(
    product_id: int,
    session: AsyncSession,
) -> ProductDB:
    product = await product_crud.get(
        obj_id=product_id,
        session=session,
    )
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Продукт не найден!'
        )
    return product


async def check_customer_order_exists(
    order_id: int,
    session: AsyncSession,
) -> None:
    customer_order = await customer_order_crud.get(
        obj_id=order_id,
        session=session,
    )
    if customer_order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Заказ не найден!'
        )
    return None


async def check_available_product_quantity(
    product_order: ProductOrderAdd,
    session: AsyncSession,
) -> None:
    product = await check_product_exists(
        product_id=product_order.product_id,
        session=session,
    )
    if product_order.quantity > product.quantity:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Отсутствует достаточное количество товара для заказа!'
        )

    return None
