from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import product_order_crud
from app.schemas.product_order import ProductOrderAdd, ProductOrderDB

from app.service import create_product_order, update_product_order

router = APIRouter()


@router.post(
    '/add',
    response_model=ProductOrderDB,
)
async def post_product_to_order(
    obj_in: ProductOrderAdd,
    session: AsyncSession = Depends(get_async_session),
):
    product_order = await product_order_crud.get_by_product_and_order(
        session=session,
        obj_data=obj_in,
    )

    if product_order:
        return await update_product_order(
            obj_in=obj_in,
            product_order=product_order,
            session=session,
        )

    return await create_product_order(
        obj_in=obj_in,
        session=session,
    )
