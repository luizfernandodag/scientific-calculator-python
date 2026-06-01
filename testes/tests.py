import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self) -> None:
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(self.calculator.subtract(10, 4), 6)

    def test_multiply(self) -> None:
        self.assertEqual(self.calculator.multiply(5, 6), 30)

    def test_divide(self) -> None:
        self.assertEqual(self.calculator.divide(20, 5), 4.0)

    def test_divide_by_zero_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
