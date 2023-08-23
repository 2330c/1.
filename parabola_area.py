import numpy
import math

#f = lambda x : 4-x**2
def f(x):
    """4-x*x"""
    return 10-2*x**5

numbers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

rect_areas = []
for number in numbers:
    y = f(number)
    print(y)

acc = 0
for w in numpy.arange(0,2,0.1):
    acc = acc + f(w)*.1
print("With 20 rects in Q1")
print("1st quadrant area",acc)
print("total area",2*acc)

acc = 0
for w in numpy.arange(0,2,0.01):
    acc = acc + f(w)*.01
print("With 200 rects in Q1")
print("1st quadrant area",acc)
print("total area",2*acc)

import numpy as np
import matplotlib.pyplot as plt

def approximate_area(a,b,n):
    """Splits the interval [a,b] into n subintervals"""
    acc = 0
    for w in numpy.arange(a,b,(b-a)/n):
        acc = acc + f(w)*(b-a)/n
    print("With",n,"rects (graphing)")
    print("1st quadrant area",acc)
    print("area",acc)

    rectangle_ys = {}
    for x in numpy.arange(a,b,(b-a)/n):
        key = f'{x:.{4}f}'
        rectangle_ys [key]=f(x)

    width = (b-a)/n
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in rectangle_ys.items():
        offset = width * multiplier
        #print("offset",offset,"offset",offset,"measurement",measurement,"width",width)
        rects = ax.bar(a+offset+.5*width, measurement, width, label=attribute)
        if n <= 60:
            ax.bar_label(rects, padding=20)
        multiplier += 1

    if n<= 10:
        ax.legend(loc='upper left')
    ax.set_xlim(a, b)
    ax.set_ylim(0, 10) #Change later?

    x = np.linspace(a,b,100)
    y = f(x)

    ax.plot(x,y)
    plt.show()

print("Will graph y="+f.__doc__+"over the specified interval.")
print("Please choose bounds between -2 and 2.")

try:
    minimum = input("What's the minimum bound?")
    minimum = float(minimum)
    if minimum < -2 or minimum > 2:
        raise AssertionError("minimum must be between -2 and 2")
    assert minimum >= -2
    maximum = input("What's the maximum bound?")
    maximum = float(maximum)
    if maximum < -2 or maximum > 2:
        raise AssertionError("maximum must be between -2 and 2")
    if maximum <= minimum:
        raise AssertionError("maximum must be greater than minimum")
    message = input("With how many rectangles?")
    n = int(message)
    approximate_area(minimum,maximum,n)
except ValueError:
    print("Not a number")
except AssertionError as e:
    print(e)