from models.order import Order
from config import CURRENCY


def format_order_summary(order: Order) -> str:
    return (
        f"Order #{order.order_id}\n"
        f"Customer ID: {order.customer_id}\n"
        f"Status: {order.status}\n"
        f"Subtotal: {order.subtotal:.2f} {CURRENCY}\n"
        f"Discount: {order.discount:.2f} {CURRENCY}\n"
        f"Total: {order.total:.2f} {CURRENCY}\n"
    )