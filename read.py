'''Create a graph from results of multiple choice quiz.'''
import csv
import datetime

with open('results.csv') as f:
    reader = csv.reader(f)
    count = 0
    xs = []
    ys = []
    ns = [] #Number of questions in the quiz
    header = next(reader)
    for row in reader:
        print(row)
        d = datetime.datetime.strptime(row[0],'%Y-%m-%d').date()
        t = datetime.datetime.strptime(row[1], '%H:%M:%S.%f').time()
        dt = datetime.datetime.combine(d,t)
        xs.append(dt)
        #xs.append(count)
        count += 1 #count = count + 1
        ys.append(float(row[5])) #int() or float()?
        ns.append(int(row[3]))


import numpy as np
import matplotlib.pyplot as plt

print(xs)
print(ys)

subsetxs = [] #For quizzes for at least 11 questions
subsetys = []
for i in range(len(ns)):
    n = ns[i]
    if n > 10:
        subsetxs.append(xs[i])
        subsetys.append(ys[i])

fig, ax = plt.subplots()
ax.plot(xs,ys)
#ax.scatter(dist3,period2)
plt.show()
