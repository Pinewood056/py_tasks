from math import sqrt


class Triangle:

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.semi_perimeter = (side_a + side_b + side_c) * 0.5

    def is_exist(self):
        if self.side_a + self.side_b < self.side_c or \
                self.side_a + self.side_c < self.side_b or \
                self.side_b + self.side_c < self.side_a:
            return False
        else:
            return True

    def square(self):
        return sqrt(self.semi_perimeter * (self.semi_perimeter - self.side_a) * 
                    (self.semi_perimeter - self.side_b) * (self.semi_perimeter - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def type(self):
        if self.side_a == self.side_b == self.side_c:
            return "Triangle is equilateral"
        elif self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c:
            return "Triangle is isosceles"
        elif self.side_a * self.side_a == self.side_b * self.side_b + self.side_c * self.side_c \
                or self.side_a * self.side_a + self.side_c * self.side_c == self.side_b * self.side_b \
                or self.side_c * self.side_c == self.side_b * self.side_b + self.side_a * self.side_a:
            return "Triangle is right"
        else:
            return "Triangle is scalene"


# You can set Triangle dimensions here
# BEFORE USE UNCOMMENT THIS SECTION
# if Triangle(side_a=10, side_b=15, side_c=17).is_exist() is True:
#    print('Square is', Triangle(side_a=10, side_b=15, side_c=17).square())
#    print('Perimeter is', Triangle(side_a=10, side_b=15, side_c=17).perimeter())
#    print(Triangle(side_a=10, side_b=15, side_c=17).type())
# else:
#    print('Triangle doesnt exist')
