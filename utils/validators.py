from models.order import Order
from repositories.product_repository import ProductRepository


def validate_order(order: Order, product_repository: ProductRepository) -> None:
    if not order.items:
        raise ValueError("Order must contain at least one item.")

    for item in order.items:
        if item.quantity <= 0:
            raise ValueError(f"Invalid quantity for product {item.product_id}.")

        product = product_repository.get_by_id(item.product_id)

        if product is None:
            raise ValueError(f"Product {item.product_id} does not exist.")

        if not product.available:
            raise ValueError(f"Product {product.name} is not available.")