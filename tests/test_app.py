import unittest

from app import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Unit tests for add_numbers()."""

    def test_two_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_positive_and_negative(self):
        self.assertEqual(add_numbers(10, -4), 6)

    def test_with_zero(self):
        self.assertEqual(add_numbers(0, 7), 7)

    def test_two_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
