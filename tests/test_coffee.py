import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_init(self):
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.name, "Espresso")  # Adjust if name is private

if __name__ == "__main__":
    unittest.main()
