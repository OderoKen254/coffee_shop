
class order:
    _all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order._all.append(self)
    
    @property
    def customer(self):
        return self._customer
    

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be a Customer instance")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee
    

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        self._coffee = value
        
    @property
    def price(self):
        return self._price
    

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number")
        if not 1.0 <= float(value) <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(value)
        
    def __repr__(self):
        return f"Order(customer={self.customer.name}, coffee={self.coffee.name}, price={self.price})"
    

        
