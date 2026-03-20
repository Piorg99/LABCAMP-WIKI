from config import DISCOUNT_PREMIUM_RATE, DISCOUNT_BULK_RATE, BULK_THRESHOLD
from models.customer import Customer


class DiscountService:
    def calculate_discount(self, customer: Customer, subtotal: float) -> float:
        discount = 0.0

        if customer.customer_type == "premium":
            discount += subtotal * DISCOUNT_PREMIUM_RATE

        if subtotal > BULK_THRESHOLD:
            discount += subtotal * DISCOUNT_BULK_RATE

        return discount