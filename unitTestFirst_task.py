import unittest
from first_task import Triangle


class TriangleTest(unittest.TestCase):
    def SetUpTriangle(self):
        self.Triangle = Triangle()

    def test_NotExist(self):
        self.assertEqual(Triangle(side_a=10, side_b=15, side_c=100).is_exist(), False)
        self.assertEqual(Triangle(side_a=15, side_b=100, side_c=10).is_exist(), False)
        self.assertEqual(Triangle(side_a=100, side_b=15, side_c=10).is_exist(), False)

    def test_square(self):
        self.assertEqual(Triangle(side_a=10, side_b=10, side_c=10).square(), 43.30127018922193)
        self.assertEqual(Triangle(side_a=10, side_b=10, side_c=15).square(), 49.607837082461074)
        self.assertEqual(Triangle(side_a=17, side_b=19, side_c=25.5).square(), 161.4999879063463)

    def test_perimeter(self):
        self.assertEqual(Triangle(side_a=10, side_b=10, side_c=10).perimeter(), 30)
        self.assertEqual(Triangle(side_a=10, side_b=10, side_c=15).perimeter(), 35)
        self.assertEqual(Triangle(side_a=17, side_b=19, side_c=25.5).perimeter(), 61.5)

    def test_type(self):
        self.assertEqual(Triangle(side_a=10, side_b=10, side_c=10).type(), "Triangle is equilateral")
        self.assertEqual(Triangle(side_a=10, side_b=10, side_c=15).type(), "Triangle is isosceles")
        self.assertEqual(Triangle(side_a=5, side_b=12, side_c=13.).type(), "Triangle is right")
        self.assertEqual(Triangle(side_a=17, side_b=19, side_c=25.5).type(), "Triangle is scalene")


if __name__ == "__main__":
  unittest.main()
