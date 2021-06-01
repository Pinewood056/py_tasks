from math import sqrt


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = (a + b + c) * 0.5

    def is_exist(self):
        if self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
            return False
        else:
            return True

    def square(self):
        return sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

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


# You can set Triangle dimensions here
# BEFORE USE UNCOMMENT THIS SECTION
# if Triangle(a=10, b=15, c=17).is_exist() is True:
#    print('Square is', Triangle(a=10, b=15, c=17).square())
#    print('Perimeter is', Triangle(a=10, b=15, c=17).perimeter())
#    print(Triangle(a=10, b=15, c=17).type())
# else:
#    print('Triangle doesnt exist')
