import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_calculator_initializes_with_right_value(self):
        calc = Calculator()
        self.assertEqual(calc.value(), 0)

    def test_add_adds_the_number_to_the_value(self):
        calc = Calculator()
        calc.add(3)
        self.assertEqual(calc.value(), 3)
    
    def test_add_accumulates_adition_operation(self):
        calc = Calculator()
        calc.add(3)
        calc.add(2)
        self.assertEqual(calc.value(), 5)



# calc.add()
# calc.value()