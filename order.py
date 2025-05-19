from customer import Customer  # Add this at the top


class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("customer must be a Customer instance")
        self.customer = customer
        self.coffee = coffee
        self.price = price
