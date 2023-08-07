import numpy
import math

numbers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

rect_areas = []
for number in numbers:
    y = (4-number**2/4)**.5

acc = 0
for w in numpy.arange(0,2,0.1):
    acc = acc + ((4-number**2/4)**.5)*.1

print("1st quadrant area",acc)
print("total area",2*acc)
print("pi*a*b",math.pi*4*2)

acc = 0
for w in numpy.arange(0,2,0.1):
    acc = acc + ((4-number**2/4)**.5)*.01

print("1st quadrant area",acc)
print("total area",2*acc)
print("pi*a*b",math.pi*4*2)

def approximate_area(n):
    acc = 0
    for w in numpy.arange(0,2,2/n):
        acc = acc + ((4-number**2/4)**.5)*2/n

    print("1st quadrant area",acc)
    print("total area",2*acc)
    print("pi*a*b",math.pi*4*2)

approximate_area(20)
approximate_area(200)