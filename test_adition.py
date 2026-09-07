import unittest

from addition import sum


class TestSum(unittest.TestCase):
    def test_sum_negative_and_positive(self):
        self.assertEqual(sum(-2, 5), 3)

    def test_sum_two_positive(self):
        self.assertEqual(sum(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
