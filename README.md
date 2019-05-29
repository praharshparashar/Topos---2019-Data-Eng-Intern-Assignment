# Topos - 2019 Data Eng Intern Assignment
In this assignment I was asked to make a scraper in either pythin or NodeJS to collect data from Wikipedia about the top cities in the United States. I chose python as my programming language. The following lines describe the approach taken by me to achieve the said objective.

NOTE:  The format of the CSV file is in UTF and NOT in UTF8 , so a manual change can be made to get the CSV in the desired format to upload in  BigQuery.

The enviornments used for the assignment are:
python3
imports include:
Pandas
bs4 to import BeautifulSoup 
requests
imported urlopen from urllib.request.

The primary task for me was to make a scraper that could extract tabular data from one page on wikipedia. The approach i took for that was as follows:

First I open a city page on wikipedia and inspected it. This gave me a general idea of the HTML layout of that page. As I don't have any prior experience with HTML, It took me some time and assistance from Google to understand how the data is arranged on a web page. 

Then i collected URL of different cities of the United States and made a list of the URL's . The scraper function which i will elaboate in the next paragraph, went through each URL one by one and scrapped the data and kept adding it to the CSV file.

Further I made a function called "scraper_trial" which performed the scarapping of the data from the wikipedia page. It searches the table mentioned in the 'class':'infobox geography vcard', and then it scarpes the data from that. The table in 'class':'infobox geography vcard' is almost the same in all the different pages of the different cities in the united states. So all the different cities share common header/title.

Following that i made a function called "longest_URL", which finds the URL which has the largest number of headers and then sets that as the common header for each subsequent cities data.  In the case of cities which had a lower number of header as compared to the common header/title, a 0 was inserted in those places.
 
 So to summerise my approach : I created 2 functions called 'longest_URL' and 'scraper_trial' which work in tandon. longest_URL find the URL which has the highest number of columns ,then the following code finds that header/title and sets them as the common title/header for the CSV file:

URL1 = 'The found URL'
req = requests.get(l_URL)
soup = BeautifulSoup(req.text, 'html.parser')
table = soup.find('table',{'class':'infobox geography vcard'})
rows = table.find_all('th')
columns = [a.text.replace('\xa0•','').replace('\xa0','') for a in rows[1:len(rows)]]
df = pd.DataFrame(columns = columns)

Then the 'scraper_trial' function is run in a for loop and is iterated for each URL . So it extracts the data part of the table, i.e the part which contains the values and information for the corresponding headers/title and appends them into the CSV format in the directed location. Its also removes the gibberish symbols and values before appending, hence cleaning the data before putting in the CSV file.


The complete code is attaced in the repository.





