#arithmatic
print("3+4",3+4,"3*4",3*4,"3^4",3**4)
print("'apple'*5",'apple'*5)
print('pencil'<'folder') #False
print('charger'<'speaker') #True
#Lexicographic (alphabetical) order.

#lists
li=[8,'tissue']
li.append('box')
print(li)
print(li*5)
li2=[3, 5, 17]
li.extend(li2)
print(li)
print(([x+x for x in li]))
print(len(li)) #6
import random
r=random.randint(0,len(li)-1)
print(r)
del li[r]
print(li)
print([type(x) for x in li])

#functions
def f(li):
    """Multiplies each off integer entry of li by 3."""
    for i in range(len(li)):
        x=li[i]
        if type(x)!=type(0):
            continue
        if x%2==1: #modulo means remainder.
            li[i]=x*3 #indexing into a list on the LHS (left-hand side): edits entry.

f(li) #back in global scope, so now li means what it meant before f.
print(li)

def g(n):
    if n%2==0:
        return n//2
    if n%2==1:
        return 3*n+1
    
seed=201
x=seed
while x>1:
    x=g(x)
    print(x)

import time
start=time.perf_counter()
results={} #This makes an empty dictionary
for seed in range(1,200000):
    it=[seed]
    while it[-1]>1: #-1 means the *last* entry of the list.
        it.append(g(it[-1]))
    results[seed]=len(it) #dictionary by key is just like list by index
#print(results)
longest_seed=max(results,key=lambda x : results[x])
print("The longest run was for",longest_seed,"with duration",results[longest_seed])
end=time.perf_counter()
print("It took",end-start,"seconds.")

import matplotlib.pyplot as plt
import numpy as np

#x=np.random.normal(170,10,250)

# Create three subplots
#ax1.set_title('Sharing Y axis')
f, (ax0, ax1, ax2, ax3) = plt.subplots(1, 4, sharey=True)

#Dictionary slicing:
#print({k:d[k] for k in l if k in d})

from scipy import stats
values0 = {k:results[k] for k in results if k%4==0}.values() #0 mod 4
values1 = {k:results[k] for k in results if k%4==1}.values() #1 mod 4
values2 = {k:results[k] for k in results if k%4==2}.values() #2 mod 4
values3 = {k:results[k] for k in results if k%4==3}.values() #2 mod 4
print("For 0 mod 4:",stats.describe(list(values0)))
print("For 1 mod 4:",stats.describe(list(values1)))
print("For 2 mod 4:",stats.describe(list(values2)))
print("For 3 mod 4:",stats.describe(list(values2)))
ax0.hist(values0)
ax1.hist(values1)
ax2.hist(values2)
ax3.hist(values3)
#plt.hist(results.values())
plt.show()

# / gives a float (floating-point number).
# // gives an integer (integer quotient --> rounds down).
# % gives the remainder.