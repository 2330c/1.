# y = (9-9*x**2/25)**.5
# True for any quadrant 1 point on the ellipse
# x**2/25 + y**2/9 = 1

# x = 0, 1/2, 1, ..., 4.5

numbers = [0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]

# You can either initialize an accumulator
# or construct a list
for number in numbers:
    y = (9-9*number**2/25)**.5
    print(y)