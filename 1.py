from math import sqrt

#a = float(input('Enter first side: '))
#b = float(input('Enter second side: '))
#c = float(input('Enter third side: '))

class Triangle:
    def __init__( self, a=6, b=6, c=9):
        self.a = a
        self.b = b
        self.c = c
        self.p = (a+b+c) * 0.5


#use Gerron to get triangle square
    def square( self ):
        return sqrt( self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
    def perimeter( self ):
        return self.p * 2
    def type(self):
        if self.a == self.b == self.c:
            return "Triangle is equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Triangle is isosceles"
        elif self.a^2 == self.b^2 + self.c^2 or self.b^2 == self.a^2 + self.c^2 or c^2 == self.b^2 + self.a^2:
            return "Triangle is right"
        else :
            return "Triangle is scalene"


try1 = Triangle()


#It`s the end for Perimeter and square
print ("Square is", try1.square())
print ("Perimeter is", try1.perimeter())
print (try1.type())
