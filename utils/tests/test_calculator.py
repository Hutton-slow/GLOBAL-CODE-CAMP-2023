from unittest import TestCase
from utils.calculator import Calculator

class CalculatorTest(TestCase):
    def test(self):
        self.assertTrue(True)

    def failingtest(self):
         self.assertTrue(False)

def test_calculator_values_int(self):
    calculator = calculator(4,5)
    int_datatype = type(calculator.num1)
    assertTrue(int_datatype == int)