### HANDS ON TASK: DAY 3 & 4

# a. Use requests + bs4 or Selenium 
# Libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By # to help select specific elements on web pages 
from selenium.webdriver.common.keys import Keys # to enable keyboard interactions with web elements
from selenium.webdriver.support.ui import Select # for selection from the drop down
import json

# b. Example Site: http://quotes.toscrape.com/search.aspx

url = "http://quotes.toscrape.com/search.aspx"

driver = webdriver.Chrome()
driver.get(url)
sleep(1)
Author = []
Quotes = []

i = 1
while True:
    try:
        select_author = driver.find_element(By.TAG_NAME, 'select')
        select_author = Select(select_author)
        if i >= len(select_author.options):
            break

        Author.append(select_author.options[i].text) 

        select_author.select_by_index(i)
        sleep(1)

        j = 1
        Quote = set()
        while True:
            try:
                select_tag = driver.find_element(By.ID, 'tag')
                select_tag = Select(select_tag)

                if j >= len(select_tag.options):
                    break
                
                select_tag.select_by_index(j)
                sleep(1)
                
                btn = driver.find_element(By.NAME, 'submit_button')
                btn.click()
                sleep(1)
                data = driver.find_element(By.CLASS_NAME, 'content')
                
                quote_text = data.text.strip().strip('“”')
                Quote.add(quote_text)
                
                print(f'Author index: {i}, Tag index: {j}')
                j += 1
                
            except:
                break
        
        Quotes.append(list(Quote))
        i += 1
        
    except:
        break


for i in range(len(Author)):
    print(Author[i])
    print(Quotes[i])

# c. Save results in .json file
results = {}
for idx in range(len(Author)):
    results[Author[idx]] = Quotes[idx]

with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

driver.quit()
