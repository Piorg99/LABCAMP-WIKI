from models.product import Product


class ProductRepository:
    def __init__(self):
        self.products = {
            1: Product(1, "Laptop", 1200.0, True),
            2: Product(2, "Mouse", 25.0, True),
            3: Product(3, "Keyboard", 70.0, True),
            4: Product(4, "Monitor", 220.0, False),
        }

    def get_by_id(self, product_id: int) -> Product | None:
        return self.products.get(product_id)