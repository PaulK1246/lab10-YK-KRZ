# https://github.com/PaulK1246/lab10-YK-KZ.git
# Partner 1: Yechan Kim
# Partner 2: Kellen Zander

import math
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 5), 8)
        self.assertEqual(calculator.add(-2, 7), 5)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.sub(10, 4), 6)
        self.assertEqual(calculator.sub(0, 5), -5)
        self.assertEqual(calculator.sub(-3, -6), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.log(10, 100), 2.0)
        self.assertAlmostEqual(calculator.log(2, 8), 3.0)
        self.assertAlmostEqual(calculator.log(4, 16), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.log(1, 10)
        with self.assertRaises(ValueError):
            calculator.log(-2, 10)
        with self.assertRaises(ValueError):
            calculator.log(2, -10)