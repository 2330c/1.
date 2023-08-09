import numpy
import math

numbers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

rect_areas = []
for number in numbers:
    y = (4-number**2/4)
    print(y)

acc = 0
for w in numpy.arange(0,2,0.1):
    acc = acc + ((4-w**2/4))*.1

print("1st quadrant area",acc)
print("total area",2*acc)
#print("pi*a*b",math.pi*4*2)

acc = 0
for w in numpy.arange(0,2,0.01):
    acc = acc + ((4-w**2/4))*.01

print("1st quadrant area",acc)
print("total area",2*acc)
#print("pi*a*b",math.pi*4*2)

def approximate_area(n):
    acc = 0
    for w in numpy.arange(0,2,2/n):
        acc = acc + ((4-w**2/4))*2/n

    print("1st quadrant area",acc)
    print("total area",2*acc)
    #print("pi*a*b",math.pi*4*2)

approximate_area(20)
approximate_area(200)
approximate_area(2000)
approximate_area(20000)

import numpy as np
import matplotlib.pyplot as plt

rectangles = (numbers)
rectangle_ys = {
    '0.1' : (3.9975),
    '0.2' : (3.99),
    '0.3' : (3.9775),
    '0.4' : (3.96),
    '0.5' : (3.9375),
    '0.6' : (3.91),
    '0.7' : (3.8775),
    '0.8' : (3.84), 
    '0.9' : (3.7975),
    '1' : (3.75),
    '1.1' : (3.6975),
    '1.2' : (3.64),
    '1.3' : (3.5775),
    '1.4' : (3.5100000000000002),
    '1.5' : (3.4375),
    '1.6' : (3.36),
    '1.7' : (3.2775,),
    '1.8' : (3.19),
    '1.9' : (3.0975),
    '2' : (3.0)}

x = np.arange(len(rectangles))
width = 0.1
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in rectangle_ys.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=20)
    multiplier += 1

ax.legend(loc='upper left', ncols=2)
ax.set_xlim(0, 2)
ax.set_ylim(0, 4)

x = np.linspace(0,5,20)
y = 4-x*x

ax.plot(x,y)
plt.show()