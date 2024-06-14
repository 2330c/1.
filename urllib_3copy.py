import urllib3
import requests
import csv
resp = urllib3.request("GET", "https://www.cia.gov/the-world-factbook/field/air-pollutants")
print(resp.status)
print(resp.data)

html_doc = resp.data
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print("soup.a",soup.a)
print("len(soup.find_all('a'))",len(soup.find_all('a')))

body_tag = soup.body
print("len(body_tag)",len(body_tag))
print("len(body_tag.contents)",len(body_tag.contents))

countryemissions = {}

for div in soup.find_all('div', class_='pb30'):
    try:
        country_name_tag = div.find('h3')
        emissions_data_tag = div.find('p')

        if country_name_tag and emissions_data_tag:
            country_name = country_name_tag.text.strip()
            emissions_data = emissions_data_tag.text.strip().split()
            emissions = float(emissions_data[0])
            year = int(emissions_data[-1])
            countryemissions[country_name] = [emissions, year]
        else:
            print("Missing h3 or p tag in div:", div)
    except Exception as e:
        print(f"Error processing data for a country: {e}")

print("Extracted emissions data:", countryemissions)

print(countryemissions)

wpp_url = 'https://population.un.org/wpp2019/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_TotalPopulationBySex.csv'


try:
    wpp_response = requests.get(wpp_url)

    if wpp_response.status_code == 200:
        print("Successfully fetched the UN WPP CSV file.")
    else:
        print(f"Failed to fetch the UN WPP CSV file. Status code: {wpp_response.status_code}")
        exit()

    csv_filename = 'WPP2019_TotalPopulationBySex.csv'
    with open(csv_filename, 'wb') as f:
        f.write(wpp_response.content)

    print(f"CSV file '{csv_filename}' saved successfully.")

    populationdict = {}

    try:
        with open('WPP2019_TotalPopulationBySex.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['Variant'] == 'Medium' and row['Time'] == '2020' and row['Sex'] == 'BothSexes':
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

except Exception as e:
    print(f"Error processing emissions data: {e}")
