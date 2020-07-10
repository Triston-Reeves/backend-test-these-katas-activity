import unittest
import katas
from katas import add, factorial, multiply, power, fibonacci


class TestKatas(unittest.TestCase):
    def test_add(self):
        """Return the result of adding x to y."""
        self.assertEqual(add(4, 7), 11)
    def test_multiply(self):
        """Return the result of multiplying x by y."""
        self.assertEqual(multiply(3, 6), 18)
    def test_power(self):
        """Return the result of taking x to the nth power."""
        self.assertEqual(power(4, 4), 256)
    def test_factorial(self):
        """Return the result of calculating the factorial of n."""
        self.assertEqual(
            [factorial(n) for n in range(6)], [1, 1, 2, 6, 24, 120])
    def test_fibonacci(self):
        """Return the nth number in the fibonacci sequence (starting at 0)."""
        # dont know 
        pass
if __name__ == '__main__':
    unittest.main()

