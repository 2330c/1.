import numpy
import math

numbers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

rect_areas = []
for number in numbers:
    y = (4-number**2)
    print(y)

acc = 0
for w in numpy.arange(0,2,0.1):
    acc = acc + ((4-w**2))*.1

print("1st quadrant area",acc)
print("total area",2*acc)
#print("pi*a*b",math.pi*4*2)

acc = 0
for w in numpy.arange(0,2,0.01):
    acc = acc + ((4-w**2))*.01

print("1st quadrant area",acc)
print("total area",2*acc)
#print("pi*a*b",math.pi*4*2)

import numpy as np
import matplotlib.pyplot as plt

def approximate_area(n):
    acc = 0
    for w in numpy.arange(0,2,2/n):
        acc = acc + ((4-w**2))*2/n

    print("1st quadrant area",acc)
    print("total area",2*acc)
    #print("pi*a*b",math.pi*4*2)

    rectangle_ys = {}
    for x in numpy.arange(0,2,2/n):
        key = f'{x:.{4}f}'
        rectangle_ys [key]=4-x**2

    width = 2/n
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in rectangle_ys.items():
        offset = width * multiplier
        print("offset",offset,"offset",offset,"measurement",measurement,"width",width)
        rects = ax.bar(offset+.5*width, measurement, width, label=attribute)
        ax.bar_label(rects, padding=20)
        multiplier += 1

    ax.legend(loc='upper left')
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 4)

    x = np.linspace(0,2,100)
    y = 4-x*x

    ax.plot(x,y)
    plt.show()

approximate_area(40)
#approximate_area(200)
#approximate_area(2000)
#approximate_area(20000)