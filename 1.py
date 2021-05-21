from math import sqrt


class Triangle:

    def __init__(self, a=float(input('Enter first side: ')), b=float(input('Enter second side: ')),
                 c=float(input('Enter third side: '))):
        self.a = a
        self.b = b
        self.c = c
        self.p = (a+b+c) * 0.5

    def is_exist(self):
        if self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
            return False
        else:
            return True

    def square(self):
        return sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    def perimeter(self):
        return self.p * 2

    def type(self):
        if self.a == self.b == self.c:
            return "Triangle is equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Triangle is isosceles"
        elif self.a * self.a == self.b * self.b + self.c * self.c \
                or self.a * self.a + self.c * self.c == self.b * self.b \
                or self.c * self.c == self.b * self.b + self.a * self.a:
            return "Triangle is right"
        else:
            return "Triangle is scalene"


if Triangle().is_exist() is True:
    print('Square is', Triangle().square())
    print('Perimeter is', Triangle().perimeter())
    print(Triangle().type())
else:
    print('Triangle doesnt exist')
