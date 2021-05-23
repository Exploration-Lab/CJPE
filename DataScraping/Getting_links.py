
import requests
import re
from bs4 import BeautifulSoup
import time
import json

URL = 'https://indiankanoon.org/browse/' # url of site from where we are scraping
page = requests.get(URL) # sending a request to the url
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all(class_ = 'browselist')
results = list(results[0:1])

links = {}
no_of_pages = list(range(100))
base = 'https://indiankanoon.org'

for link in results: # loop for multiple courts, if scraping data from multiple courts
    linkd = link.find('a')['href']
    court_name = link.find('a').text
    URL = base+linkd
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    result_new = soup.find_all(class_ = 'browselist')
    links[court_name] = []
    for link_new in result_new: # loop for every year
        print((link_new.find('a').text) + " Year Started .....\n")
        if((int)(link_new.find('a').text) < 1947 or (int)(link_new.find('a').text) > 2020):
            continue
        URL = base + link_new.find('a')['href']
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        result_new2 = soup.find_all(class_ = 'browselist')
        for link_new2 in result_new2: # loop for every month
            for page_in in no_of_pages: # loop for every page
              time.sleep(1)
              URL = base + link_new2.find('a')['href']
              URL = URL + '&pagenum={}'.format(page_in)
              page = requests.get(URL)
              soup = BeautifulSoup(page.content, 'html.parser')
              result_new3 = soup.find_all(class_ = 'result_url')
              if(len(result_new3) == 0):
                break
              for link_new3 in result_new3: # finally appending the url in the list
                URL = base + link_new3['href']
                links[court_name].append(URL)
        print("Current Year Completed\n")


valid_court_name = ['Supreme Court of India']

final_list = {}
for court_name in valid_court_name:
  final_list[court_name] = links[court_name]


json_object = json.dumps(final_list, indent = 4) 

# saving the dictionary with links in a json file
with open("links_Supreme_Court.json", "w") as outfile:  
    outfile.write(json_object)

