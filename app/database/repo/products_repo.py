from typing import List
from app.database.models.cart import Cart
from app.database.models.products import Product
from fastapi import HTTPException, status
from app.core.config.constants import status_messages
from beanie import PydanticObjectId
from beanie.operators import In

async def check_existing_product(name: str) -> bool:
    existing_product = await Product.find_one(Product.name == name)
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=status_messages["product_conflict"]
        )
    return False

async def find_product_by_id(product_id: str) -> Product:
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=status_messages["product_not_found"]
        )
    return product

async def get_or_create_cart(user_id: PydanticObjectId) -> Cart:
    cart = await Cart.find_one(Cart.user_id == user_id)
    if not cart:
        cart = Cart(user_id=user_id ,items=[])
        await cart.insert()
    return cart

async def get_products_by_ids(product_ids: List[PydanticObjectId]) -> List[Product]:
    products = await Product.find(In(Product.id, product_ids)).to_list()
    return products