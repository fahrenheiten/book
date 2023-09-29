import unittest

def rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError('Width and height must be non-negative')
    return width * height

class TestRectangleArea(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_zero_value(self):
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            rectangle_area(-4, 5)

if __name__ == "__main__":
    unittest.main()

