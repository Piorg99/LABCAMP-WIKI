from models.customer import Customer
from models.order import Order
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from services.discount_service import DiscountService
from services.pricing_service import PricingService
from utils.validators import validate_order


class OrderService:
    def __init__(
        self,
        product_repository: ProductRepository,
        order_repository: OrderRepository,
        pricing_service: PricingService,
        discount_service: DiscountService,
    ):
        self.product_repository = product_repository
        self.order_repository = order_repository
        self.pricing_service = pricing_service
        self.discount_service = discount_service

    def process_order(self, order: Order, customer: Customer) -> Order:
        validate_order(order, self.product_repository)

        subtotal = self.pricing_service.calculate_subtotal(order)
        discount = self.discount_service.calculate_discount(customer, subtotal)
        total = subtotal - discount

        order.subtotal = subtotal
        order.discount = discount
        order.total = total
        order.status = "PROCESSED"

        self.order_repository.save(order)

        return order