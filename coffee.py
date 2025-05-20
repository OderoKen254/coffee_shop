
class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

    def __repr__(self):
        return f"Coffee({self.name}, {self.price})"
    def __eq__(self, other):
        if isinstance(other, Coffee):
            return self.name == other.name and self.price == other.price
        return False
    def __hash__(self):
        return hash((self.name, self.price))
    def __lt__(self, other):
        if isinstance(other, Coffee):
            return self.price < other.price
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Coffee):
            return self.price <= other.price
        return NotImplemented