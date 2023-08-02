import numpy

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

print("The areas for each rectangle: ")
for number in numbers:
    a = ((9-9*number**2/25)**.5)*.5
    print(a)

print("The area of the ellipse: ")

def sum (x):
    return x + a

def sigma(f):
    acc = 0
    for w in numpy.arange(0,4.5,0.5):
        acc = acc + w
    return acc

print(sigma(a))