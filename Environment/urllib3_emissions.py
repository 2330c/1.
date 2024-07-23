import urllib3
#import requests
import time
import csv
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