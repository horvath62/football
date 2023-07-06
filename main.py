
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DRIVER_PATH = 'c:\chrome'
#driver = webdriver.Chrome('C:/chrome')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://google.com')






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
