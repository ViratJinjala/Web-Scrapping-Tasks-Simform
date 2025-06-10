### HANDS ON TASK: DAY 3 & 4

# Libraries
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd 

## Task 1-a. Scrape a Paginated Site (e.g. http://books.toscrape.com/)
## Task 1-b. Follow pagination links across multiple pages

url = "http://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

Title = []
Price = []
Rating = []
Avail = []

for _ in range(20):
    # i. Book Title
    titles = soup.find_all('h3')
    for title in titles:
        Title.append(title.text.strip())

    # ii. Book Price
    prices = soup.find_all('p', class_ = "price_color")
    for price in prices:
        Price.append(price.text.strip()[1:])

    # iii. Book Rating
    D = {
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5
    }
    ratings = soup.find_all('p', class_ = "star-rating")
    for rating in ratings:
        Rating.append(D[rating.get("class")[1]])

    # iv. Availability
    avails = soup.find_all('p', class_ = "instock availability")
    for avail in avails:
        Avail.append("Available" if avail.text.strip()=='In stock' else "Not Available")

    print(f"Abstracted data from the page: {url}")

    next_btn = soup.select_one('li.next a')
    if next_btn:
        url = urljoin(url, next_btn['href'])
    else:
        break
    


    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


Final = pd.DataFrame({"Title":Title,
                      "Price":Price,
                      "Rating":Rating,
                      "Availability":Avail})

print(Final)