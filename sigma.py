"""For sigma notation."""

def square(x):
    return x**2

def cube(x):
    return x**3

def fourth_power(x):
    return x**4

def sigma(f,lb,ub):
    """Returns the sum of f(k) as k goes from lb to ub, inclusive"""
    acc = 0
    for k in range(lb,ub+1):
        acc = acc + f(k)
    return acc

print("sigma(square,-9,9):",sigma(square,-9,9))

print("sigma(lambda x: x**2-2*x+2),2,9):",sigma((lambda x: x**2-2*x+2),2,9))