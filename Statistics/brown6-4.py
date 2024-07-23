import numpy
import math

# y = (9-9*x**2/25)**.5
# True for any quadrant 1 point on the ellipse
# x**2/25 + y**2/9 = 1

# x = 0, 1/2, 1, ..., 4.5

numbers = [0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]

# You can either initialize an accumulator
# or construct a list
rect_areas = []
for number in numbers:
    y = (9-9*number**2/25)**.5
    print(y)

acc = 0
for w in numpy.arange(0,5,0.5):
    acc = acc + ((9-9*w**2/25)**.5)*.5

print("1st quadrant area",acc)
print("total area",4*acc)
print("pi*a*b",math.pi*5*3)

acc = 0
for w in numpy.arange(0,5,0.05):
    acc = acc + ((9-9*w**2/25)**.5)*.05

print("1st quadrant area",acc)
print("total area",4*acc)
print("pi*a*b",math.pi*5*3)

def approximate_area(n):
    "n is the number of rectangles to use"
    acc = 0
    for w in numpy.arange(0,5,5/n): #was 0.05 for n=100
        acc = acc + ((9-9*w**2/25)**.5)*5/n #was 0.05 for n=100

    print("1st quadrant area",acc)
    print("total area",4*acc)
    print("pi*a*b",math.pi*5*3)

approximate_area(1000)
approximate_area(10000)