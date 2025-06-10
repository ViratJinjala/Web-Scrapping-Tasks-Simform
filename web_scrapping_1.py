### HANDS ON TASK: DAY 1 & 2

# Libraries
import requests
from bs4 import BeautifulSoup


## Task 1-a. Use requests to load a static page.
URL = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(URL).text
print(response)

## Task 1-b. Use BeautifulSoup to extract all <h1>, <h2>, and <a href> links.
# data = soup.find()
# data = soup.find_all("p", class_="your-class", id="your-id", string="some text",s attrs={"data-attr": "value"}, limit=5)

soup = BeautifulSoup(response, 'html.parser')
data1 = soup.find_all(['h1','h2'])
data2 = soup.find_all('a',attrs={'href': True})
print(data1)
print(data2)


# Task 2 : Parse Structured Data from a simple blog or news site

URL = "https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2laeGZhV0RoRjNrZjl6ajNFQVZ5Z0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
response = requests.get(URL).text

soup = BeautifulSoup(response,'html.parser')

# i. Extract Article titles
titles = soup.find_all('h4',class_ = 'ipQwMb ekueJc RD0gLb')
Titles = []
for title in titles:
    Titles.append(title.text)
print(Titles)

# ii. URLs
urls = soup.find_all('a',class_ = 'DY5T1d RZIKme')
URLs = []
for url in urls:
    URLs.append(str("https://news.google.com/" + url.get('href')[2:]))
print(URLs)

# iii. Date published
dates = soup.find_all('div',class_ = 'SVJrMe')
DATE = []
for date in dates:
    DATE.append(date.text[:date.text.lower().find('ago')+3])
print(DATE)