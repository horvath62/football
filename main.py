
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# driver.get('https://scrapingclub.com/')
driver.get('https://www.espn.com/college-football/playbyplay/_/gameId/401411092')

'''
PlayList = driver.find_elements(By.CLASS_NAME, 'PlayListItem')
for play in PlayList:
    print(play.text)
'''

time.sleep(3) # Sleep for 3 seconds

Collapse = driver.find_element(By.CLASS_NAME, 'AccordianPanel')

time.sleep(10) # Sleep for 3 seconds

driver.quit()

'''
import requests
from requests_html import HTMLSession

import certifi
print (certifi.where())

# url = 'https://www.espn.com/college-football/playbyplay/_/gameId/401019470'
# url = 'https://www.espn.com/college-football/scoreboard'
url = 'https://python.org/'

try:
    session = HTMLSession()
    response = session.get(url, verify=False)

except requests.exceptions.RequestException as e:
    print("exception:", e)



title=response.html.find('title')
print(title)


fname = football.html
obj = requests.get(url)
open(temp.html, 'w')
'''
