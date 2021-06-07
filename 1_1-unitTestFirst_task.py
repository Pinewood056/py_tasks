import unittest
from first_task import Triangle


class TriangleTest(unittest.TestCase):
    def SetUpTriangle(self):
        self.Triangle = Triangle()

    def test_NotExist(self):
        self.assertEqual(Triangle(a=10, b=15, c=100).is_exist(), False)
        self.assertEqual(Triangle(a=15, b=100, c=10).is_exist(), False)
        self.assertEqual(Triangle(a=100, b=15, c=10).is_exist(), False)

    def test_square(self):
        self.assertEqual(Triangle(a=10, b=10, c=10).square(), 43.30127018922193)
        self.assertEqual(Triangle(a=10, b=10, c=15).square(), 49.607837082461074)
        self.assertEqual(Triangle(a=17, b=19, c=25.5).square(), 161.4999879063463)

    def test_perimeter(self):
        self.assertEqual(Triangle(a=10, b=10, c=10).perimeter(), 30)
        self.assertEqual(Triangle(a=10, b=10, c=15).perimeter(), 35)
        self.assertEqual(Triangle(a=17, b=19, c=25.5).perimeter(), 61.5)

    def test_type(self):
        self.assertEqual(Triangle(a=10, b=10, c=10).type(), "Triangle is equilateral")
        self.assertEqual(Triangle(a=10, b=10, c=15).type(), "Triangle is isosceles")
        self.assertEqual(Triangle(a=5, b=12, c=13.).type(), "Triangle is right")
        self.assertEqual(Triangle(a=17, b=19, c=25.5).type(), "Triangle is scalene")


if __name__ == "__main__":
  unittest.main()
