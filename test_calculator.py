# https://github.com/PaulK1246/lab10-YK-KZ.git
# Partner 1: Yechan Kim
# Partner 2: Kellen Zander

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 10)  # base 1 is invalid
        with self.assertRaises(ValueError):
            calculator.log(-2, 10)  # base < 0
        with self.assertRaises(ValueError):
            calculator.log(2, -10)  # log of negative number

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(0), 0.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)