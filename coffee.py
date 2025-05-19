class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._orders = []

    @property
    def name(self):
        return self._name  # Immutable after init

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if self._orders:
            return sum(order.price for order in self._orders) / len(self._orders)
        return 0
