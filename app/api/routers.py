from fastapi import APIRouter

from app.api.endpoints import product_order_router

main_router = APIRouter()
main_router.include_router(
    product_order_router, prefix='/product_order', tags=['product_order']
)
