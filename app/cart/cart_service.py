from beanie import PydanticObjectId
from app.core.constants import success_messages
from app.models.cart import CartItem
from app.database.repo.products_repo import find_product_by_id, get_or_create_cart
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
            if item.product.id == data.product_id:
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