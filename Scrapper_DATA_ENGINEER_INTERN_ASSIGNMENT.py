#importing of differnt files which are used in this assignment are taking place
import pandas as pd
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


def scraper_trial(URL):

    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    # This is used to find the table from which the information has to be extracted
    table = soup.find('table',{'class':'infobox geography vcard'})
    rows1 = table.find_all('tr')
    tds = []
    tds = [a.find_all('td') for a in rows1[7:len(rows1)]]
    values = []
    # this is done to remove any garbage values and null values in the table that cause an error
    for i in range(len(tds)):
        try:
            values.insert(i,tds[i][0].text.replace('\xa0','').replace('\n','').replace('\xa0sq\xa0mi','')
                          .replace('\xa0km2','').replace('/km2','').replace('âˆ’','').replace('','').replace('â€“',''))
        except IndexError:
            values.insert(i,'0')
    return values

    def longest_URL(URL_list):
        count = 0
        Biggest_URL = []
        for URL in URL_list:

            req = requests.get(URL)
            soup = BeautifulSoup(req.text, 'html.parser')

            # here the process of comparing the of the length of the common header/title is taking place

            table = soup.find('table',{'class':'infobox geography vcard'})
            rows = table.find_all('th')
            current = len(rows)
            if (current >= count):
                count = current
                Biggest_URL = URL
            # the url with the biggest header/title and its size is returned.
        return Biggest_URL, count

        # here the code is made for one city to show the basic logic of the scrapper
  URL1 = 'https://en.wikipedia.org/wiki/New_York_City'
  URL_list= []
  URL_list.append(URL1)
  l_URL = []
  l_URL,count = longest_URL(URL_list)
  print(l_URL)
  print(count)
  #This portion of the code is used to make the common header/title of the CSV file
URL1 = 'https://en.wikipedia.org/wiki/New_York_City'
req = requests.get(l_URL)
soup = BeautifulSoup(req.text, 'html.parser')
table = soup.find('table',{'class':'infobox geography vcard'})
#Find the common header/title
rows = table.find_all('th')
#here the clearing of the data is done
columns = [a.text.replace('\xa0•','').replace('\xa0','') for a in rows[1:len(rows)]]
df = pd.DataFrame(columns = columns)
# here the URL's of differnet cities can be entered as a list
URL_list= []
URL_list.append(URL1)
URL_list.append(URL2)
URL_list.append(URL3)
# Output for different cities can taken .
for j in URL_list:

    scraper_out = scraper_trial(j)
    print(scraper_out)
    df = df.append(pd.Series(scraper_out, index = columns), ignore_index = True)

# this is done to store the output in CSV format in a destined location
df.to_csv(r'/Users/praharshparashara/Documents/GitHub/Topos---2019-Data-Eng-Intern-Assignment/cities.csv', index = False)
