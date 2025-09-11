from fastapi import APIRouter, status, Depends
from .products_service import product_service
from app.schemas.products_schema import (
    ProductsSchema,
    UpdateProductSchema,
    ProductResponse,
    ProductsResponse,
    MessageResponse
)
from app.core.security.role_guard import RoleGuard
from app.database.models.user import Roles
admin_access = RoleGuard(allowed_roles=[Roles.ADMIN])
product_access = RoleGuard(allowed_roles=[Roles.PRODUCT_ADMIN, Roles.ADMIN])

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new product",
    response_model=ProductResponse,
    dependencies=[Depends(admin_access)],
)
async def create_product(data: ProductsSchema):
    return await product_service.create_product(data)

@router.get(
    "/all",
    status_code=status.HTTP_200_OK,
    summary="Get all products",
    response_model=ProductsResponse,
)
async def get_all_products():
    return await product_service.get_all_products()

@router.get(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    summary="Get a product",
    response_model=ProductResponse,
)
async def get_product(product_id: str):
    return await product_service.get_product_by_id(product_id)

@router.patch(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    summary="Update a product",
    response_model=ProductResponse,
    dependencies=[Depends(product_access)],
)
async def update_product(product_id: str, product: UpdateProductSchema):
    return await product_service.update_product_by_id(product_id, product)

@router.delete(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a product",
    response_model=MessageResponse,
    dependencies=[Depends(product_access)],
)
async def delete_product(product_id: str):
    return await product_service.delete_product(product_id)