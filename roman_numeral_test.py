import unittest
from roman_numeral import romanise

class TestStringMethods(unittest.TestCase):
    def test_does_one(self):
        self.assertEqual(romanise(1), "I")