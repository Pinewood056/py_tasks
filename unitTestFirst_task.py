from first_task import Triangle
from math import sqrt

a = 10
b = 10
c = 10
bb = 15
cc = 15
aaa = 17
bbb = 19
ccc = 19
a1 = 100
b1 = 150
c1 = 200
c2 = 25.5

print('3 Triangles, that can`t exist')
# Triangle isn`t exist if 'a+b<c' OR 'a+c<b' OR 'b+c<a'
# This Triangle shouldn`t exist. This code should return 'Triangle doesnt exist'
if Triangle(a, bb, c1).is_exist() is True:
    print(Triangle(a, bb, c1).type())
else:
    print('Triangle doesnt exist')

if Triangle(a, b1, ccc).is_exist() is True:
    print(Triangle(a, b1, ccc).type())
else:
    print('Triangle doesnt exist')

if Triangle(a1, b, cc).is_exist() is True:
    print(Triangle(a1, b, cc).type())
else:
    print('Triangle doesnt exist')

print('Triangle with a=10, b=10, c=10')
# Square for Triangle with dimensions 10, 10, 10 = 43,3. Perimeter is 15. This Triangle type is equilateral
if Triangle(a, b, c).is_exist() is True:
    print('Square is', Triangle(a, b, c).square())
    print('Perimeter is', Triangle(a, b, c).perimeter())
    print(Triangle(a, b, c).type())

print('Triangle with a=10, b=10, c=15')
# Square for Triangle with dimensions 10, 10, 15 = 49,6. Perimeter is 17,5. This Triangle type is isosceles
if Triangle(a, b, cc).is_exist() is True:
    print('Square is', Triangle(a, b, cc).square())
    print('Perimeter is', Triangle(a, b, cc).perimeter())
    print(Triangle(a, b, cc).type())

print('Triangle with a=17, b=19, c=25.5')
# Square for Triangle with dimensions 17, 25.5, 19 = 161.5. Perimeter is 61.5. This Triangle type is right
if Triangle(aaa, bbb, c2).is_exist() is True:
    print('Square is', Triangle(aaa, bbb, c2).square())
    print('Perimeter is', Triangle(aaa, bbb, c2).perimeter())
    print(Triangle(aaa, bbb, c2).type())
