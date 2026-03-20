from models.order import Order
from repositories.product_repository import ProductRepository


def validate_order(order: Order, product_repository: ProductRepository) -> None:
    if not order.items:
        raise ValueError("Order must contain at least one item.")

    for item in order.items:
        # TODO 1:
        # controllare che la quantity sia > 0

        product = product_repository.get_by_id(item.product_id)

        # TODO 2:
        # controllare che il prodotto esista

        # TODO 3:
        # controllare che il prodotto sia disponibile