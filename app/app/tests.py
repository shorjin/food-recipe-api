"""
Sample tests
"""
# Import necessary modules and functions. SimpleTestCase for tests
# without a database,and TestCase for tests involving a database
from django.test import SimpleTestCase
# 2. Import objects to test from the 'app' module.
from app import calc


# 3. Define a test class.
#    Create a test class named 'CalcTests' that inherits from 'SimpleTestCase'.
class CalcTests(SimpleTestCase):
    """Test the calc module"""
    # 4. Add a test method.
    #    Define a test method named 'test_add_numbers'.
    def test_add_numbers(self):
        """Testing adding numbers together"""
        # 5. Setup inputs. No setup required in this case.

        # 6. Execute the code to be tested.
        res = calc.add(5, 6)

        # Use 'self.assertEqual' to check if the result (res) is equal to 11.
        self.assertEqual(res, 11)

    # Test-driven development (TDD): Write the test first.
    def test_subtract_numbers(self):
        """Testing subtracting numbers together"""
        # 5. Setup inputs. No setup required in this case.

        # 6. Execute the code to be tested.
        res = calc.subtract(15, 10)

        # Use 'self.assertEqual' to check if the result (res) is equal to 5.
        self.assertEqual(res, 5)
