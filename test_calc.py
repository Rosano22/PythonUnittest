import unittest
import calc

class TestCalc(unittest.TestCase): # our class TestCalc inherits from unittest.TestCase
    # The methods in this class needs to start with test_...
    # if the methods don't start with test_... they won't run

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(0, 2), 2)
        self.assertEqual(calc.add(-7, 5), -2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(0, 2), 0)
        self.assertEqual(calc.multiply(-7, 5), -35)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 4), 2.5)
        self.assertEqual(calc.divide(0, 2), 0)
        self.assertEqual(calc.divide(1, 1), 1)

        self.assertRaises(ValueError, calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide(4, 0)


if __name__ == '__main__':
    unittest.main()