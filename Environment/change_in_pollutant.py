"""Shows how the production of a given pollutant changed over time. First, we get parameter names containing the substring 'PM2.5' as an initital substring in the Annual Concentration By Monitor CSV. When 'PM2.5' showed up elsewhere, it seemed to always be a specific pollutant (titanium, tungsten, etc.)"""

#This CSV doesn't have 'PM25' without the dot.

import csv
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

pm25namecount = defaultdict(int) # #times each string containing 'PM2.5' shows up
#For a dd of type int, its default values are 0 (unless otherwise specified).

pm25local = defaultdict(list) #Keys are state FIPS, values list of Arithmetic Means.
#Don't forget to look at the units, sample duration, etc., anything else that could matter!
#TODO.

with open("annual_conc_by_monitor_2023.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    param_name_index = header.index('Parameter Name')
    print(param_name_index)
    state_code_index = header.index('State Code') #0 for Column A
    print(state_code_index)
    AM_index = header.index('Arithmetic Mean') #27 for Column AB
    print(AM_index)
    for row in reader:
        parameter_name = row[param_name_index]
        if 'PM2.5' in parameter_name and parameter_name.index('PM2.5')==0:
            pm25namecount[parameter_name] += 1
        if parameter_name == "PM2.5 - Local Conditions":
             AM = row[AM_index]
             state_code = int(row[state_code_index])
             if len(AM) > 0:
                  AM = float(AM)
                  pm25local[state_code].append(AM)

print(pm25namecount)
print(len(pm25namecount))
for state_code in sorted(pm25local.keys()):
     avg = sum(pm25local[state_code])/len(pm25local[state_code])
     print(state_code, '\t', len(pm25local[state_code]),'\t', avg) #The number of observations from that state
    #The number of observations from that state and the average of arithmetic means.

#Running this, we have determined that Pm2.5 - Local Conditions should suffice for gathering data.

abbrev = {}

pm25emissions = defaultdict(list) #For each state, a list of years.

with open("state_tier1_08feb2024_ktons.csv") as f:
    reader = csv.reader(f)
    next(reader)
    header = next(reader)
    print(header)
    state_code_index = header.index("State FIPS")
    years = range(2002,2024) #Later: can we go back to 1990?
    yearstrings = ["emissions"+str(y) for y in years]
    year_indices = [header.index(s) for s in yearstrings] #17 to 33, representing col's R thru AH.
    abbrev_index = header.index("State")
    pollutant_index = header.index("Pollutant")
    for row in reader:
        pollutant = row[pollutant_index]
        if "PM25" not in pollutant:
            continue
        state_code = int(row[state_code_index])
        if not pm25emissions[state_code]: #if this list is empty,
            pm25emissions[state_code]=[0.0 for x in years]
        state_abbrev = row[abbrev_index]
        abbrev[state_code] = state_abbrev
        try:
            emissions = [float(row[i]) for i in year_indices] #list of emissions
            for i in range(len(years)): #0-21 inclusive
                pm25emissions[state_code][i] += emissions[i] #We are adding each year's PM25emissions-of-that-source to the state's PM25emissions for the corresponding year.
        except ValueError as e:
            print(f"Skipping row: {row}, Error: {e}")
        except Exception as e:
            print(e)

#Alabama? pm25emissions[1] should be the y-values, 22 y-values
plt.figure(figsize=(8, 6))
plt.plot(years, pm25emissions[36], '-o')
plt.show()

#Find inspiration for what to do next at PM25_copy.py