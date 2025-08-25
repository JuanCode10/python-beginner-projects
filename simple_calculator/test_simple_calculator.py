# Import the unittest module
import unittest
# Import the functions to be tested
from simple_calculator.simple_calculator import add, subtract, multiply, divide, power, square_root, cube_root, show_history


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the simple calculator functions"""

    def test_add_method(self):
        """Test the add function"""
        test_cases = [
            ("Add positive numbers", 1, 2, 3),
            ("Add negative numbers", -1, -2, -3),
            ("Add negative and positive numbers", -1, 1, 0),
            ("Add zeros", 0, 0, 0),
            ("Add decimal numbers", 2.5, 2.5, 5.0)
        ]
        for txt, a, b, expected in test_cases:
            with self.subTest(msg=txt, a=a, b=b, expected=expected):
                self.assertEqual(add(a, b), expected)

    def test_subtract_method(self):
        """Test the subtract function"""
        test_cases = [
            ("Subtract positive numbers", 5, 3, 2),
            ("Subtract negative numbers", -5, -3, -2),
            ("Subtract negative and positive numbers", -5, 3, -8),
            ("Subtract zeros", 0, 0, 0),
            ("Subtract decimal numbers", 5.5, 2.5, 3.0)
        ]
        for txt, a, b, expected in test_cases:
            with self.subTest(msg=txt, a=a, b=b, expected=expected):
                self.assertEqual(subtract(a, b), expected)

    def test_multiply_method(self):
        """Test the multiply function"""
        test_cases = [
            ("Multiply positive numbers", 2, 3, 6),
            ("Multiply negative numbers", -2, -3, 6),
            ("Multiply negative and positive numbers", -2, 3, -6),
            ("Multiply by zero", 5, 0, 0),
            ("Multiply decimal numbers", 2.5, 2.0, 5.0)
        ]
        for txt, a, b, expected in test_cases:
            with self.subTest(msg=txt, a=a, b=b, expected=expected):
                self.assertEqual(multiply(a, b), expected)

    def test_divide_method(self):
        """Test the divide function"""
        test_cases = [
            ("Divide positive numbers", 6, 3, 2),
            ("Divide negative numbers", -6, -3, 2),
            ("Divide negative and positive numbers", -6, 3, -2),
            ("Divide decimal numbers", 5.0, 2.0, 2.5)
        ]
        for txt, a, b, expected in test_cases:
            with self.subTest(msg=txt, a=a, b=b, expected=expected):
                self.assertEqual(divide(a, b), expected)
    
    def test_divide_by_zero(self):
        """Test division by zero"""
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(divide(5, 0), "Error: Division by zero")

    def test_power_method(self):
        """Test the power function"""
        test_cases = [
            ("Power of positive numbers", 2, 3, 8),
            ("Power of negative base", -2, 3, -8),
            ("Power of negative exponent", 2, -3, 0.125),
            ("Power of zero exponent", 5, 0, 1),
            ("Power of decimal numbers", 2.5, 2, 6.25)
        ]
        for txt, a, b, expected in test_cases:
            with self.subTest(msg=txt, a=a, b=b, expected=expected):
                self.assertEqual(power(a, b), expected)

    def test_square_root_method(self):
        """Test the square_root function"""
        test_cases = [
            ("Square root of positive number", 9, 3),
            ("Square root of zero", 0, 0),
            ("Square root of decimal number", 2.25, 1.5)
        ]
        for txt, a, expected in test_cases:
            with self.subTest(msg=txt, a=a, expected=expected):
                self.assertEqual(square_root(a), expected)

    def test_square_root_of_negative(self):
        """Test square root of negative number"""
        with self.assertRaises(ValueError):
            self.assertEqual(square_root(-4), "Error: Cannot compute square root of negative number")

    def test_cube_root_method(self):
        """Test the cube_root function"""
        test_cases = [
            ("Cube root of positive number", 27, 3),
            ("Cube root of negative number", -27, -3),
            ("Cube root of zero", 0, 0),
            ("Cube root of decimal number", 8.0, 2.0)
        ]
        for txt, a, expected in test_cases:
            with self.subTest(msg=txt, a=a, expected=expected):
                self.assertEqual(cube_root(a), expected)

    def test_show_history_method(self):
        """Test the show_history function"""
        test_cases = [
            ("Empty history", [], "No operations performed yet."),
            ("Single operation in history", ["Added 1 and 2 to get 3"], "All operations performed so far:\n\tAdded 1 and 2 to get 3"),
            ("Multiple operations in history", ["Added 1 and 2 to get 3", "Subtracted 5 from 10 to get 5"], "All operations performed so far:\n\tAdded 1 and 2 to get 3\n\tSubtracted 5 from 10 to get 5")
        ]
        for txt, history, expected in test_cases:
            with self.subTest(msg=txt, history=history, expected=expected):
                from io import StringIO
                import sys

                # Capture the output of show_history
                captured_output = StringIO()
                sys.stdout = captured_output
                show_history(history)
                sys.stdout = sys.__stdout__
                self.assertEqual(captured_output.getvalue().strip(), expected)
    