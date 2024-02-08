import unittest

from Solutions import is_palindrome


class TestSolutions(unittest.TestCase):

    def test_is_palindrome(self):
        input = "amanaplanacanalpanama"
        self.assertTrue(is_palindrome(input), msg=None)

    if __name__ == '__main__':
        unittest.main()
