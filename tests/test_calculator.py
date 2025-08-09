"""
Unit tests for the Calculator class.
"""

import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_calculator_initialization(self):
        """Test that calculator initializes correctly."""
        self.assertIsInstance(self.calc, Calculator)
        self.assertEqual(self.calc.history, [])
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
        self.assertIn("5 + 3 = 8", self.calc.get_history())
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)
        self.assertIn("-5 + -3 = -8", self.calc.get_history())
    
    def test_add_mixed_numbers(self):
        """Test addition with mixed positive and negative numbers."""
        result = self.calc.add(10, -4)
        self.assertEqual(result, 6)
        self.assertIn("10 + -4 = 6", self.calc.get_history())
    
    def test_add_floats(self):
        """Test addition with floating point numbers."""
        result = self.calc.add(2.5, 3.7)
        self.assertAlmostEqual(result, 6.2, places=7)
    
    def test_add_invalid_types(self):
        """Test addition with invalid types."""
        with self.assertRaises(TypeError):
            self.calc.add("5", 3)
        with self.assertRaises(TypeError):
            self.calc.add(5, "3")
        with self.assertRaises(TypeError):
            self.calc.add(None, 5)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)
        self.assertIn("10 - 3 = 7", self.calc.get_history())
    
    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        result = self.calc.subtract(3, 10)
        self.assertEqual(result, -7)
        self.assertIn("3 - 10 = -7", self.calc.get_history())
    
    def test_subtract_floats(self):
        """Test subtraction with floating point numbers."""
        result = self.calc.subtract(5.5, 2.3)
        self.assertAlmostEqual(result, 3.2, places=7)
    
    def test_subtract_invalid_types(self):
        """Test subtraction with invalid types."""
        with self.assertRaises(TypeError):
            self.calc.subtract("10", 3)
        with self.assertRaises(TypeError):
            self.calc.subtract(10, [])
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        result = self.calc.multiply(4, 5)
        self.assertEqual(result, 20)
        self.assertIn("4 * 5 = 20", self.calc.get_history())
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = self.calc.multiply(10, 0)
        self.assertEqual(result, 0)
        self.assertIn("10 * 0 = 0", self.calc.get_history())
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        result = self.calc.multiply(-3, -4)
        self.assertEqual(result, 12)
        result2 = self.calc.multiply(-3, 4)
        self.assertEqual(result2, -12)
    
    def test_multiply_floats(self):
        """Test multiplication with floating point numbers."""
        result = self.calc.multiply(2.5, 4.0)
        self.assertEqual(result, 10.0)
    
    def test_multiply_invalid_types(self):
        """Test multiplication with invalid types."""
        with self.assertRaises(TypeError):
            self.calc.multiply("4", 5)
        with self.assertRaises(TypeError):
            self.calc.multiply(4, {})
    
    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
        self.assertIn("10 / 2 = 5.0", self.calc.get_history())
    
    def test_divide_with_remainder(self):
        """Test division with remainder."""
        result = self.calc.divide(10, 3)
        self.assertAlmostEqual(result, 3.3333333333333335, places=7)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        result = self.calc.divide(-10, 2)
        self.assertEqual(result, -5.0)
        result2 = self.calc.divide(10, -2)
        self.assertEqual(result2, -5.0)
        result3 = self.calc.divide(-10, -2)
        self.assertEqual(result3, 5.0)
    
    def test_divide_floats(self):
        """Test division with floating point numbers."""
        result = self.calc.divide(7.5, 2.5)
        self.assertEqual(result, 3.0)
    
    def test_divide_invalid_types(self):
        """Test division with invalid types."""
        with self.assertRaises(TypeError):
            self.calc.divide("10", 2)
        with self.assertRaises(TypeError):
            self.calc.divide(10, "2")
    
    def test_power_positive_numbers(self):
        """Test power operation with positive numbers."""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
        self.assertIn("2 ^ 3 = 8", self.calc.get_history())
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        result = self.calc.power(5, 0)
        self.assertEqual(result, 1)
    
    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        result = self.calc.power(2, -2)
        self.assertEqual(result, 0.25)
    
    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        result = self.calc.power(9, 0.5)
        self.assertEqual(result, 3.0)
    
    def test_power_invalid_types(self):
        """Test power with invalid types."""
        with self.assertRaises(TypeError):
            self.calc.power("2", 3)
        with self.assertRaises(TypeError):
            self.calc.power(2, "3")
    
    def test_history_tracking(self):
        """Test that history is properly tracked."""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        self.calc.multiply(2, 4)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 3)
        self.assertIn("1 + 2 = 3", history)
        self.assertIn("5 - 3 = 2", history)
        self.assertIn("2 * 4 = 8", history)
    
    def test_clear_history(self):
        """Test clearing the calculation history."""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        self.assertGreater(len(self.calc.get_history()), 0)
        
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)
    
    def test_get_history_returns_copy(self):
        """Test that get_history returns a copy, not the original list."""
        self.calc.add(1, 2)
        history = self.calc.get_history()
        history.append("Modified externally")
        
        # Original history should not be modified
        original_history = self.calc.get_history()
        self.assertNotIn("Modified externally", original_history)
    
    def test_chained_operations(self):
        """Test multiple operations in sequence."""
        # Test a sequence: (10 + 5) - 3 * 2 / 4 ^ 2
        result1 = self.calc.add(10, 5)  # 15
        result2 = self.calc.subtract(result1, 3)  # 12
        result3 = self.calc.multiply(result2, 2)  # 24
        result4 = self.calc.divide(result3, 4)  # 6
        result5 = self.calc.power(result4, 2)  # 36
        
        self.assertEqual(result5, 36)
        self.assertEqual(len(self.calc.get_history()), 5)


if __name__ == '__main__':
    unittest.main()