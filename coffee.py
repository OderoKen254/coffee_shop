
class Coffee:
    _all = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Coffee._all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be at between 3 and 25 characters long")
        self._name = value
    
    def orders(self):
        return [order for order in Order._all if order.coffee == self]
    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(order.price for order in orders) / len(orders)





  