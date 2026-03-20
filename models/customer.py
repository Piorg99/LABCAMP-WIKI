from dataclasses import dataclass


@dataclass
class Customer:
    customer_id: int
    name: str
    customer_type: str  # "regular" or "premium"