import sys
import os

# Print current working directory and sys.path
print("Working Directory:", os.getcwd())
print("sys.path:")
for path in sys.path:
    print(" ", path)

# Test if your modules can be imported
try:
    from coffee import Coffee
    print("Successfully imported Coffee from coffee module")
except Exception as e:
    print("Error importing Coffee from coffee module:", e)

try:
    from customer import Customer
    print("Successfully imported Customer from customer module")
except Exception as e:
    print("Error importing Customer from customer module:", e)

try:
    from order import Order
    print("Successfully imported Order from order module")
except Exception as e:
    print("Error importing Order from order module:", e)

# Check if the tests directory exists
test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests'))
print("Test path exists?", os.path.isdir(test_path))