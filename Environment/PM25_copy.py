"""First, we get parameter names containing the substring 'PM2.5' as an initital substring in the Annual Concentration By Monitor CSV. When 'PM2.5' showed up elsewhere, it seemed to always be a specific pollutant (titanium, tungsten, etc.)"""

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

pm25emissions = defaultdict(float)

with open("state_tier1_08feb2024_ktons.csv") as f:
    reader = csv.reader(f)
    next(reader)
    header = next(reader)
    print(header)
    state_code_index = header.index("State FIPS")
    twentytwentythree_index = header.index("emissions2023")
    abbrev_index = header.index("State")
    pollutant_index = header.index("Pollutant")
    for row in reader:
        pollutant = row[pollutant_index]
        if "PM25" not in pollutant:
            continue
        state_code = int(row[state_code_index])
        state_abbrev = row[abbrev_index]
        abbrev[state_code] = state_abbrev
        try:
            emissions = float(row[twentytwentythree_index])
            pm25emissions[state_code] += emissions
        except ValueError as e:
            #print(f"Skipping row: {row}, Error: {e}")
            pass

population = {}
with open("populationsbystate.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        state_abbrev = row[0]
        population[state_abbrev] = int(row[2])

normalized_pm25_emissions = defaultdict(float) #by population
avg_pm25_concentrations = defaultdict(float) #averaging all monitoring stations

for state_code in pm25emissions: #keys: FIPS
    if state_code in pm25local: #keys: FIPS
        state_abbrev = abbrev[state_code]
        if state_abbrev in population: #keys: two-letter abbreviations
            print("For state_code",state_code)
            emissions_per_capita = pm25emissions[state_code] / population[state_abbrev]
            concentrations_avg = np.mean(pm25local[state_code])
            normalized_pm25_emissions[state_code] = emissions_per_capita
            avg_pm25_concentrations[state_code] = concentrations_avg

#print(abbrev)

#for state_code in sorted(pm25local.keys()):
     #if state_code not in abbrev:
          #continue
     #avg = sum(pm25local[state_code])/len(pm25local[state_code])
     #print(abbrev[state_code], '\t', len(pm25local[state_code]),'\t', avg)

x_values = []
y_values = []
state_codes = []

for state_code in normalized_pm25_emissions.keys(): #For making lists out of dictionaries and keeping them collated.
    if state_code in avg_pm25_concentrations:
        x_values.append(normalized_pm25_emissions[state_code])
        y_values.append(avg_pm25_concentrations[state_code])
        state_codes.append(state_code)

try:
    correlation_coef = np.corrcoef(x_values, y_values)[0, 1]
    print(f"Correlation coefficient: {correlation_coef}")
except ValueError as e:
    print(f"ValueError: {e}")

plt.figure(figsize=(8, 6))
plt.xlim(0,max(x_values)*1.2)
plt.scatter(x_values, y_values, alpha=0.5)
plt.title('Correlation between Normalized PM2.5 Emissions and Average Observed PM2.5 Levels')
plt.xlabel('Normalized PM2.5 Emissions')
plt.ylabel('Average Observed PM2.5 Levels')
plt.grid(True)
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(abbrev[state_codes[int(sel.target.index)]]))
plt.tight_layout()
plt.show()