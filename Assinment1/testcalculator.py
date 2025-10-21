import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(3, 2), 5)
        self.assertEqual(Calculator.add(4, 4), 8)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(3, 2), 1)
        self.assertEqual(Calculator.subtract(5, 5), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(4, 3), 12)
        self.assertEqual(Calculator.multiply(5, 5), 25)

    def test_divide(self):
        self.assertEqual(Calculator.divide(9, 3), 3)
        self.assertEqual(Calculator.divide(5, 5), 1)


    if __name__ == '__main__':
        unittest.main()
