import unittest
from roman_numeral import romanise

class TestStringMethods(unittest.TestCase):
    def test_does_one(self):
        self.assertEqual(romanise(1), "I")

    def test_does_two(self):
        self.assertEqual(romanise(2), "II")

    def test_does_three(self):
        self.assertEqual(romanise(3), "III")