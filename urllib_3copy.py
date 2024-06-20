import urllib3
#import requests
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
resp = urllib3.request("GET", "https://www.cia.gov/the-world-factbook/field/air-pollutants")
print(resp.status)
#print(resp.data)

html_doc = resp.data
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#print("soup.a",soup.a)
#print("len(soup.find_all('a'))",len(soup.find_all('a')))

body_tag = soup.body
#print("len(body_tag)",len(body_tag))
#print("len(body_tag.contents)",len(body_tag.contents))

countryemissions = {} #keys = country_name; values = [amount, year]
#This is only keeping track of carbon dioxide emissions

#i=0
for div in soup.find_all('div', class_='pb30'):
    #i+=1
    #if i>=10:
        #break
    try:
        country_name_tag = div.find('h3')
        for emissions_type in div.find_all('strong'):
            if country_name_tag and emissions_type:
                country_name = country_name_tag.text.strip()
                sibling_soup = emissions_type.next_sibling
                emissions_type = emissions_type.text.strip()
                #emissions = float(emissions_type[0])
                #year = int(emissions_type[-1])
                #countryemissions[country_name] = [emissions, year]
                sibling_soup = sibling_soup.split()
                amount = float(sibling_soup[0].replace(",", ""))
                units = " ".join(sibling_soup[1:-2])
                year = int(sibling_soup[-2][1:])
                #print(emissions_type, country_name, sibling_soup, amount, units, year)
                specific_emissions_type = emissions_type
                if specific_emissions_type == 'carbon dioxide emissions:':
                    countryemissions[country_name] = [amount, year]
                    if units == 'megatons':
                        pass
                    else:
                        print("NOT OK")
            else:
                print("Missing h3 or p tag in div:", div)
    except Exception as e:
        print(f"Error processing data for a country: {e}")
        #print(emissions_type, country_name, sibling_soup, amount, units, year)
print("Extracted emissions data:", countryemissions)

print(countryemissions)

wpp_url = 'https://population.un.org/wpp2019/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_TotalPopulationBySex.csv'


try:
    resp = urllib3.request("GET", wpp_url)

    if resp.status == 200:
        print(type(resp.status))
        print("Successfully fetched the UN WPP CSV file.")
    else:
        print(f"Failed to fetch the UN WPP CSV file. Status code: {resp.status}")
        exit()

    csv_filename = 'WPP2019_TotalPopulationBySex.csv'
    with open(csv_filename, 'wb') as f:
        f.write(resp.data)

    print(f"CSV file '{csv_filename}' saved successfully.")

    time.sleep(1)

    populationdict = {} #keys: country_names; values: total_population

    try:
        with open('WPP2019_TotalPopulationBySex.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                if len(row) < 9:
                    continue
                if row['Variant'] == 'Medium' and row['Time'] == '2020':
                    country = row['Location']
                    total_population = int(float(row['PopTotal']))
                    populationdict[country] = total_population

        print("Extracted population data:", populationdict)

    except Exception as e:
        print(f"Error processing CSV file: {e}")

    print(populationdict)

    emissionspercapita = {}

    for country, data in countryemissions.items():
        emissions, year = data
        population = populationdict.get(country, None)

        if population:
            percapita = emissions / (population / 1000000)
            emissionspercapita[country] = [emissions, year, population, percapita]

    for country, data in emissionspercapita.items():
        print(f"{country}: Emissions = {data[0]} Mt, Year = {data[1]}, Population = {data[2]}, Per Capita = {data[3]:.2f} Mt per million people")

except Exception as e:
        print(f"Error occurred: {e}")

countries = list(emissionspercapita.keys())
populations = [emissionspercapita[country][2] for country in countries]
emissions = [emissionspercapita[country][0] for country in countries]

plt.figure(figsize=(14, 8))
plt.scatter(populations, emissions, alpha=0.5)

m, b = np.polyfit(populations, emissions, 1)
plt.plot(populations, m * np.array(populations), color='red')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Population')
plt.ylabel('Carbon Emissions (Mt)')
plt.title('Population vs Carbon Emissions')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

emissions_per_capita_sorted = sorted(emissionspercapita.items(), key=lambda x: x[1][3], reverse=True)
top_10_worst = emissions_per_capita_sorted[:10]
top_10_best = emissions_per_capita_sorted[-10:]

mean_per_capita = np.mean([data[3] for data in emissionspercapita.values()])
median_per_capita = np.median([data[3] for data in emissionspercapita.values()])

print("\nTop 10 countries with the worst emissions per capita:")
for country, data in top_10_worst:
    print(f"{country}: {data[3]:.2f} Mt per million people")

print("\nTop 10 countries with the best emissions per capita:")
for country, data in top_10_best:
    print(f"{country}: {data[3]:.2f} Mt per million people")

print(f"\nMean emissions per capita: {mean_per_capita:.2f} Mt per million people")
print(f"Median emissions per capita: {median_per_capita:.2f} Mt per million people")