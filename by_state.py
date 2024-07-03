"""The numbers reported are in kilotons."""
import csv, matplotlib.pyplot as plt, numpy as np, mplcursors

with open("state_tier1_08feb2024_ktons.csv") as f:
    reader = csv.reader(f)
    next(reader)
    header = next(reader)
    print(header)
    ammoniabystate = {}
    blackcarbonbystate = {}
    statecol = header.index("State") #1 in this ver.
    polcol = header.index("Pollutant") #4 in this ver.
    twentyfourteen = header.index("emissions2014")
    for row in reader:
        #Add state abbrev. as key if not present, augment value if already present.
        state = row[statecol] #2-let. abbrev.
        pollutant = row[polcol]
        weight = row[twentyfourteen] #kilotons produced in 2014
        if len(weight) > 0:
                weight = float(weight)
        else:
            continue
        if pollutant == "NH3":
            if state not in ammoniabystate:
                ammoniabystate[state] = weight
            else:
                ammoniabystate[state] += weight
        elif pollutant == "Black Carbon": 
            if state not in blackcarbonbystate:
                blackcarbonbystate[state] = weight
            else:
                blackcarbonbystate[state] += weight
    print("Ammonia by state:", ammoniabystate)
    print("Black carbon by state:", blackcarbonbystate)

with open("populationsbystate.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    population = {}
    for row in reader:
        population[row[0]] = int(row[2]) #Population in 2014.
    print(population)

normalizedammonia = {}
normalizedblackcarbon = {}
for state in population:
    if state in ammoniabystate:
        perpersonammonia = ammoniabystate[state]/population[state] #kilotons per capita
        normalizedammonia[state] = perpersonammonia
    if state in blackcarbonbystate:
        perpersonblackcarbon = blackcarbonbystate[state]/population[state] #kilotons per capita
        normalizedblackcarbon[state] = perpersonblackcarbon
print("Normalized ammonia:", normalizedammonia)
print("Normalized black carbon:", normalizedblackcarbon)

ammoniavalues = []
blackcarbonvalues = []
states = []

for state in normalizedammonia:
    if state in normalizedblackcarbon:
        ammoniavalues.append(normalizedammonia[state])
        blackcarbonvalues.append(normalizedblackcarbon[state])
        states.append(state)

if ammoniavalues and blackcarbonvalues:
    fig, ax = plt.subplots()
    scatter = ax.scatter(ammoniavalues, blackcarbonvalues)

    ax.set_xlabel('Normalized Ammonia Emissions (kilotons per capita)')
    ax.set_ylabel('Normalized Black Carbon Emissions (kilotons per capita)')
    ax.set_title('Normalized Emissions Per Capita by State')

    cursor = mplcursors.cursor(scatter, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(states[sel.target.index]))

    plt.legend()
    plt.savefig('bystate.png')
    plt.show()

    correlation_coefficient = np.corrcoef(ammoniavalues, blackcarbonvalues)[0, 1]
    print("Correlation coefficient (r) between normalized ammonia and black carbon emissions:", correlation_coefficient)

    minammoniastate = min(normalizedammonia, key=normalizedammonia.get)
    maxammoniastate = max(normalizedammonia, key=normalizedammonia.get)
    minblackcarbonstate = min(normalizedblackcarbon, key=normalizedblackcarbon.get)
    maxblackcarbonstate = max(normalizedblackcarbon, key=normalizedblackcarbon.get)

    print("State with minimum normalized ammonia emissions:", minammoniastate)
    print("State with maximum normalized ammonia emissions:", maxammoniastate)
    print("State with minimum normalized black carbon emissions:", minblackcarbonstate)
    print("State with maximum normalized black carbon emissions:", maxblackcarbonstate)

    sortedammonia = sorted(normalizedammonia, key=normalizedammonia.get)
    sortedblackcarbon = sorted(normalizedblackcarbon, key=normalizedblackcarbon.get)

    print("Sorted states by normalized ammonia emissions:")
    for state in sortedammonia:
        print(state,'\t',normalizedammonia[state]*2000000) # lbs. per capita

    print("Sorted states by normalized black carbon emissions:")
    for state in sortedblackcarbon:
        print(state,'\t',normalizedblackcarbon[state]*2000000) # lbs. per capita

else:
    print("Insufficient data to plot or calculate correlation.")

#minstate = min(normalized, key = lambda x: normalized[x])
#maxstate = max(normalized, key = lambda x: normalized[x])
#print(minstate)
#print(maxstate)
#sorteddict = sorted(normalized, key = lambda x: normalized[x])
#print(sorteddict)
#for state in sorteddict:
    #print(state,'\t', normalized[state])
    #print(state,'\t',normalized[state]*2000000) #lbs. per capita