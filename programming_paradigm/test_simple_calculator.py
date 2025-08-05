#!/usr/bin/env python3
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-7, -3), -4)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(-4, 4), -16)
        self.assertEqual(self.calc.multiply(-4, -4), 16)
        self.assertEqual(self.calc.multiply(0, 4), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(4, 10), 0.4)
    
    def test_divide_by_zero(self):
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()