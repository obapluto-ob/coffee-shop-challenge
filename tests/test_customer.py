import unittest
from customer import Customer  # Import the class to be tested

class TestCustomer(unittest.TestCase):

    def test_init(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")  # Check name is set correctly

if __name__ == "__main__":
    unittest.main()
