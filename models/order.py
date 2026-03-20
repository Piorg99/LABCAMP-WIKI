from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class OrderItem:
    product_id: int
    quantity: int


@dataclass
class Order:
    order_id: int
    customer_id: int
    items: List[OrderItem]
    subtotal: float = 0.0
    discount: float = 0.0
    total: float = 0.0
    status: str = "CREATED"
    notes: Dict = field(default_factory=dict)