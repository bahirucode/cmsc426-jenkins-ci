import unittest
from app import add_numbers


class TestApp(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(add_numbers(2, 3), 6)

    def test_positive_and_negative(self):
        self.assertEqual(add_numbers(10, -4), 6)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 7), 7)

    def test_negative(self):
        self.assertEqual(add_numbers(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
