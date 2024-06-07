import csv
import random

with open("death-rate-from-malnutrition-ghe.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    perhunthous = {} # annual deaths rate from malnutrition per 100,000 by country & year.
    li = [] #list of the same.
    for row in reader:
        countryyear = (row[0], row[2])
        number = float(row[3])
        perhunthous[countryyear] = number
        li.append(number)
    print(len(perhunthous))
    li = sorted(li)
    print("len(li)",len(li))
    #print the decile
    decile_indices = [x*len(li)//10 for x in range(10)] #list comprehension
    deciles = [li[i] for i in decile_indices]
    print("deciles",deciles)
    print("end",li[-1])