import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_calculator_initializes_with_right_value(self):
        calc = Calculator()
        self.assertEqual(calc.value(), 0)

    def test_add_adds_the_number_to_the_value(self):
        calc = Calculator()
        calc.sum(3)
        self.assertEqual(calc.value(), 3)
    
    def test_add_accumulates_adition_operation(self):
        calc = Calculator()
        calc.sum(3)
        calc.sum(2)
        self.assertEqual(calc.value(), 5)
    
    def test_raises_an_error_if_number_is_not_received(self):
        calc = Calculator()

        with self.assertRaises(TypeError):
            calc.sum("3")
    
    def test_add_accepts_floating_numbers(self):
        calc = Calculator()
        calc.sum(3)
        calc.sum(2.2)
        self.assertEqual(calc.value(), 5.2)

    def test_add_allows_chaining_operations(self):
        calc = Calculator()
        calc.sum(3).sum(2)
        self.assertEqual(calc.value(), 5)
