import unittest
# Простая функция для примера
def parse_int(s):
    return int(s)
class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')