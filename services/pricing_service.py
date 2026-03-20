from models.order import Order
from repositories.product_repository import ProductRepository


class PricingService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def calculate_subtotal(self, order: Order) -> float:
        subtotal = 0.0

        for item in order.items:
            product = self.product_repository.get_by_id(item.product_id)
            subtotal += product.price * item.quantity

        return subtotal