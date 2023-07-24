dist_AU = [0.387,0.722,1,1.52,5.2,9.58,19.2,30.1,39.5] #3 sig figs
#avg. dist is semimajor axis!
period_yr = [0.241,0.615,1,1.88,11.9,29.5,84,165,249]
print(len(dist_AU),len(period_yr))

#dist3 = [x**3 for x in dist_AU] #List comprehension
dist3 = []
for x in dist_AU:
    dist3.append(x**3)

period2 = []
for y in period_yr:
    period2.append(y**2)

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#ax.plot(xs,ys)
ax.scatter(dist3,period2),
plt.show()