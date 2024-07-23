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

planets_au = [0.4,0.7,1,1.5,5.2,9.6,19.2,30,39.5] #Including Pluto

def get_stats(planets_au):
    avg_dist = sum(planets_au)/len(planets_au)
    print("avg_dist", avg_dist)

    #Using list comprehensions
    square_diffs = [(x-avg_dist)**2 for x in planets_au]
    print("square_diffs", square_diffs)

    variance = sum(square_diffs)/len(square_diffs)
    print("variance",variance)

    stdev = variance**.5
    print("std. dev.",stdev)

get_stats(planets_au)

bpm_before = [56,64,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,80,88]
bpm_after = [80,80,84,84,88,88,88,92,92,92,96,96,100,100,100,104,104,104,108,108,112,112]

get_stats(bpm_before)
get_stats(bpm_after)