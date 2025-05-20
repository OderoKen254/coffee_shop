
class Customer:
    _all = []

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.orders = []
        Customer._all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 3 <= len(value) <= 25:
            raise ValueError("Name must be at between 3 and 25 characters long")
        self._name = value

    def orders(self):
        return [order for order in Order._all if order.customer == self]
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        return Order(self, coffee, price)
    

    




    
    
    
  


