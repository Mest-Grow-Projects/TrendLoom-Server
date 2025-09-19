from typing import List
from app.database.models.cart import Cart
from app.database.models.products import Product
from fastapi import HTTPException, status
from app.core.config.constants import status_messages
from app.database.models.user import User
from beanie.operators import In
from beanie import PydanticObjectId

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

async def get_or_create_cart(user: User) -> Cart:
    cart = await Cart.find_one(
        Cart.user_id == user.id,
        fetch_links=True
    )
    if cart:
        return cart

    new_cart = Cart(user_id=user, items=[])
    await new_cart.insert()
    return new_cart

async def get_products_by_ids(product_ids: List[str]) -> List[Product]:
    if not product_ids:
        return []

    try:
        object_ids = []
        for pid in product_ids:
            try:
                object_ids.append(PydanticObjectId(pid))
            except Exception:
                continue

        if not object_ids:
            return []

        products = await Product.find(In(Product.id, object_ids)).to_list()
        return products

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )