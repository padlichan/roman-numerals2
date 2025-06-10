import unittest
from roman_numeral import romanise

class TestOutputsRoman(unittest.TestCase):
    def test_does_one(self):
        self.assertEqual(romanise(1), "I")

    def test_does_two(self):
        self.assertEqual(romanise(2), "II")

    def test_does_three(self):
        self.assertEqual(romanise(3), "III")

    def test_does_four(self):
        self.assertEqual(romanise(4), "IV")

    def test_does_ten(self):
        self.assertEqual(romanise(10), "X")

    def test_does_eighteen(self):
        self.assertEqual(romanise(18), "XVIII")

    def test_does_100(self):
        self.assertEqual(romanise(100), "C")
    
    def test_does_298(self):
        self.assertEqual(romanise(298), "CCXCVIII")
    
    def test_does_1000(self):
        self.assertEqual(romanise(1000), "M")

    def test_does_1001(self):
        self.assertEqual(romanise(1001), "MI")

    def test_does_3999(self):
        self.assertEqual(romanise(3999), "MMMCMXCIX")

class TestEdgeCases(unittest.TestCase):
    def test_doesnt_4000(self):
        self.assertRaises(ValueError, romanise, 4000)
    
    def test_doesnt_minus(self):
        self.assertRaises(ValueError, romanise, -1)