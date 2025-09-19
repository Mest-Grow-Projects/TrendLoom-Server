from beanie import PydanticObjectId
from app.core.config.constants import success_messages
from app.database.models.cart import CartItem
from app.database.repo.products_repo import (
    find_product_by_id,
    get_or_create_cart,
    get_products_by_ids,
)
from app.database.repo.user_repo import find_user_by_id
from app.schemas.cart_schema import AddToCartRequest
from app.core.config.logging_config import logger


class CartService:
    async def add_to_cart(
        self,
        user_id: str,
        data: AddToCartRequest
    ):
        await find_product_by_id(data.product_id)
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


    async def remove_from_cart(self, user_id: str, product_id: str):
        product = await find_product_by_id(product_id)
        cart = await get_or_create_cart(user_id)

        cart.items = [item for item in cart.items if item.product_id != product.id]
        await cart.save()
        return cart


    async def get_from_cart(self, user_id: str):
        try:
            user = await find_user_by_id(user_id)
            cart = await get_or_create_cart(user)
            if not cart.items:
                return {
                    "items": [],
                    "total_price": 0.0,
                    "user_id": cart.user_id
                }

            products_ids = []
            for item in  cart.items:
                try:
                    if item.product_id and hasattr(item.product_id, "id"):
                        products_ids.append(str(item.product_id.id))
                except Exception as e:
                    logger.error("Invalid product_id in cart item: %s", e)
                    continue

            if not products_ids:
                return {
                    "message": "No valid products in cart",
                    "data": {
                        "items": [],
                        "total_price": 0.0,
                        "user_id": cart.user_id
                    }
                }

            products = await get_products_by_ids(products_ids)
            product_map = { str(product.id): product for product in products }

            detailed_items = []
            total_price = 0.0

            for item in cart.items:
                try:
                    product_details = product_map.get(item.product_id)
                    if product_details and product_details.price is not None:
                        item_total = product_details.price * item.quantity
                        detailed_items.append({
                            "product": product_details.model_dump(),
                            "quantity": item.quantity,
                            "item_total": round(item_total, 2),
                        })
                        total_price += item_total
                except Exception as e:
                    logger.error("Error processing cart item: %s", e)
                    continue

            return {
                "message": "Cart products fetched successfully",
                "data": {
                    "user_id": str(cart.user_id.id) if hasattr(cart.user_id, "id") else str(cart.user_id),
                    "total_price": round(total_price, 2),
                    "items": detailed_items,
                }
            }
        except Exception as e:
            return {
                "message": f"Error fetching cart: {str(e)}",
                "data": {
                    "items": [],
                    "total_price": 0.0,
                    "user_id": user_id
                }
            }

cart_service = CartService()