# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(add_one(5), 6)

    def test_add_two(self):
        self.assertEqual(add_one(6), 7)

    def test_add_three(self):
        self.assertEqual(add_one(7), 8)

    def test_add_failed(self):
        self.assertEqual(add_one(8), 8)


if __name__ == '__main__':
    unittest.main()
