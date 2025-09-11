from app.schemas.products_schema import ProductsSchema, UpdateProductSchema
from app.database.models.products import Product
from app.core.config.constants import success_messages, status_messages
from fastapi import HTTPException, status
from app.database.repo.products_repo import check_existing_product, find_product_by_id


class ProductsService:
    async def create_product(self, data: ProductsSchema):
        await check_existing_product(data.name)

        product = Product(
            name=data.name,
            description=data.description,
            price=data.price,
        )
        await product.insert()

        return {
            "message": success_messages["product"],
            "data": product,
        }


    async def get_all_products(self):
        products = await Product.find_all().to_list()

        return {
            "message": success_messages["all_products"],
            "data": products,
        }


    async def get_product_by_id(self, product_id: str):
        if not product_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=status_messages["product_id_required"],
            )

        product = await find_product_by_id(product_id)
        return {
            "message": success_messages["find_product"],
            "data": product,
        }


    async def update_product_by_id(self, product_id: str, data: UpdateProductSchema):
        if not product_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=status_messages["product_id_required"],
            )

        updated_product = await find_product_by_id(product_id)
        updated_data = data.model_dump(exclude_unset=True, exclude_none=True)

        if not updated_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=status_messages["update_invalid"],
            )

        await updated_product.set(updated_data)

        return {
            "message": success_messages["update_product"],
            "data": updated_product,
        }


    async def delete_product(self, product_id: str):
        if not product_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=status_messages["product_id_required"],
            )

        product = await find_product_by_id(product_id)
        await product.delete()
        return { "message": success_messages["delete_product"] }

product_service = ProductsService()