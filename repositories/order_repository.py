from models.order import Order


class OrderRepository:
    def __init__(self):
        self.orders = []

    def save(self, order: Order) -> None:
        self.orders.append(order)

    def get_all(self) -> list[Order]:
        return self.orders