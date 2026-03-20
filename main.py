from models.customer import Customer
from models.order import Order, OrderItem
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from services.discount_service import DiscountService
from services.order_service import OrderService
from services.pricing_service import PricingService
from utils.formatter import format_order_summary


def main():
    product_repository = ProductRepository()
    order_repository = OrderRepository()
    pricing_service = PricingService(product_repository)
    discount_service = DiscountService()

    order_service = OrderService(
        product_repository=product_repository,
        order_repository=order_repository,
        pricing_service=pricing_service,
        discount_service=discount_service,
    )

    customer = Customer(customer_id=101, name="Alice", customer_type="premium")

    order = Order(
        order_id=1,
        customer_id=customer.customer_id,
        items=[
            OrderItem(product_id=2, quantity=2),
            OrderItem(product_id=3, quantity=1),
        ],
    )

    processed_order = order_service.process_order(order, customer)
    print(format_order_summary(processed_order))


if __name__ == "__main__":
    main()