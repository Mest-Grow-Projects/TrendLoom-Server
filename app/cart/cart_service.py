from beanie import PydanticObjectId
from app.core.constants import success_messages
from app.models.cart import CartItem
from app.database.repo.products_repo import (
    find_product_by_id,
    get_or_create_cart,
    get_products_by_ids,
)
from app.database.repo.user_repo import find_user_by_id
from app.schemas.cart_schema import AddToCartRequest


class CartService:
    async def add_to_cart(
            self,
            user_id: PydanticObjectId,
            data: AddToCartRequest
    ):
        await find_user_by_id(str(user_id))
        await find_product_by_id(str(data.product_id))
        cart = await get_or_create_cart(user_id)

        cart_item_exists = False
        for item in cart.items:
            if item.product_id == data.product_id:
                item.quantity += data.quantity
                cart_item_exists = True
                break

        if not cart_item_exists:
            cart.items.append(CartItem(product_id=data.product_id, quantity=data.quantity))

        await cart.save()
        return {
            "message": success_messages["cart_added"],
            "data": cart
        }


    async def remove_from_cart(self, user_id: PydanticObjectId, product_id: PydanticObjectId):
        cart = await get_or_create_cart(user_id)
        cart.items = [item for item in cart.items if item.product_id != product_id]
        await cart.save()
        return cart


    async def get_from_cart(self, user_id: PydanticObjectId):
        cart = await get_or_create_cart(user_id)
        if not cart.items:
            return {
                "items": [],
                "total_price": 0.0,
                "user_id": cart.user_id
            }

        product_ids = [item.product_id for item in cart.items]
        products = await get_products_by_ids(product_ids)
        product_map = { product.id: product for product in products }

        detailed_items = []
        total_price = 0.0

        for item in cart.items:
            product_details = product_map.get(item.product_id)
            if product_details:
                item_total = product_details.price * item.quantity
                detailed_items.append({
                    "product": product_details.model_dump(),
                    "quantity": item.quantity,
                    "item_total": round(item_total, 2),
                })
                total_price += item_total

        return {
            "message": "Cart products fetched successfully",
            "data": {
                "user_id": str(cart.user_id),
                "total_price": round(total_price, 2),
                "items": detailed_items,
            }
        }

cart_service = CartService()