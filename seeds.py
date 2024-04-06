n = input('Number of seeds?:')
p = input('What is the probability?:')
print('The number of seeds is ' + n + ' and the probability is ' + p)
n=int(n)
p=float(p)
import math
for k in range(0,n+1):
    print("The probabilty of ", k, "seeds is ",math.comb(n,k)*p**k*(1-p)**(n-k))