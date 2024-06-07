#random secret mean and s.d. ABV of the kegs,
#which we will be trying to guess.
import random, math
import numpy as np
mu = random.random()
si = random.random()
def f(x):
    """normal distribution"""
    return 1/(2*math.pi*si**2)**0.5*math.exp(-(x-mu)**2/(2*si**2))

def area(g,a,b,n=40):
    """find the area under g from a to b sampling n points"""
    width=(b-a)/n #width of each rectangle
    sp=np.linspace(a,b-width,n)
    retval=0
    for x in sp:
        retval+=g(x)*width
    return retval

print("mu",mu)
print("si",si)
print("area",area(f,mu-7*si,mu+7*si))
#The above print lines should be commented out

#Define a way below to *sample* individuals from the distribution.
#One way: generate a random number from 0 to 1.
#Make a "cumulative area" function that keeps counting up area
#and checking whether the area got above that random number.
#whenever the area first exceeds that random number,
#return the x-value you were at.
#This is a reasonable way to generate random individuals
#from the distribution.