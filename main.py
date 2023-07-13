
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time

driver = webdriver.Chrome()

# driver.get('https://scrapingclub.com/')
driver.get('https://www.espn.com/college-football/playbyplay/_/gameId/401403989')

'''
PlayList = driver.find_elements(By.CLASS_NAME, 'PlayListItem')
for play in PlayList:
    print(play.text)
'''

time.sleep(3) # Sleep for 3 seconds

# Collapse first drive playlist (because it default is expanded, remaining playlists are collapsed)
#DriveFirst = driver.find_element(By.CLASS_NAME, "AccordionHeader")
DriveFirst = driver.find_element(By.CLASS_NAME, "AccordionPanel.Panel")
D1 = DriveFirst.find_element(By.CLASS_NAME, 'AccordionHeader__Left')
D1.click()
# print("#", D1.text)

# Find all the drives
DriveList = driver.find_elements(By.CLASS_NAME, 'AccordionPanel.Panel')

# Now expand all play lists by clicking the drive header
for drive in DriveList:
    driveHeader = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left')
    driveHeader.click()
    time.sleep(1)

# Now get Headline, description and plays of each drive
for drive in DriveList:
    DriveHeadline = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left__Drives__Headline')
    DriveDesc = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left__Drives__Description')
    new_string = ', '.join((DriveDesc.text).split('\n'))
    print("###",DriveHeadline.text,"->",new_string)
    PlayList = drive.find_elements(By.CLASS_NAME, 'PlayListItem')
    new_string = ', '.join((drive.text).split('\n'))
    print("##",new_string)
    for play in PlayList:
        new_string = ', '.join((play.text).split('\n'))
        print("#",play.text)


'''
try:
    PlayList = driver.find_elements(By.CLASS_NAME, 'PlayListItem')
except NoSuchElementException:
    # ??? exception is not correctly handled ???
    print("No such element")

for play in PlayList:
    print(play.text)
'''


time.sleep(10) # Sleep for 3 seconds

driver.quit()



'''
driver.find_element_by_xpath('//div[@class="css-ais6tt"]//button[3]')
                              //*[text()='Começa a new game']
link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='p-5']/div[4]/button[1]")))

<input type="text" name="passwd" id="passwd-id" />
element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")
XPATH only the first will be returned. if none: a NoSuchElementException will be raised.

element.click()


<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
<html>

login_form = driver.find_element(By.XPATH, "/html/body/form[1]")
login_form = driver.find_element(By.XPATH, "//form[1]")

try:
    driver.find_element(By.XPATH, "(//*[contains(@class, 'needsclick')]//div[@role='dialog']//button)[1]").click()
except:
    print('modal not shown')


'''



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
