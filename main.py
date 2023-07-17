
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException, TimeoutException, ElementClickInterceptedException

import time

exception = False

driver = webdriver.Chrome()

# driver.get('https://scrapingclub.com/')
driver.get('https://www.espn.com/college-football/playbyplay/_/gameId/401403989')

'''
PlayList = driver.find_elements(By.CLASS_NAME, 'PlayListItem')
for play in PlayList:
    print(play.text)
'''

time.sleep(0.5) # Sleep

# Collapse first drive playlist (because it default is expanded, remaining playlists are collapsed)
try:
    DriveFirst = driver.find_element(By.CLASS_NAME, "AccordionPanel.Panel")
    D1 = DriveFirst.find_element(By.CLASS_NAME, 'AccordionHeader__Left')
    D1.click()
except NoSuchElementException:
    print("Exception: No Such Element")
    exception = True
except ElementClickInterceptedException:
    print("Exception: Element Click Intercepted")
    exception = True


# Find all the "football" drives, put into DriveList
try:
    DriveList = driver.find_elements(By.CLASS_NAME, 'AccordionPanel.Panel')
except NoSuchElementException:
    print("Exception: No Such Element")
    exception = True
except ElementClickInterceptedException:
    print("Exception: Element Click Intercepted")
    exception = True

# Now expand all play lists in each drive by clicking the drive header
for drive in DriveList:
    try:
        driveHeader = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left')
        driveHeader.click()
    except NoSuchElementException:
        print("Exception: No Such Element")
        exception = True
    except ElementClickInterceptedException:
        print("Exception: Element Click Intercepted")
        print("Try increasing sleep time between clicks to allow html page to re-render")
        exception = True
    time.sleep(0.2)
    print("##", DriveList)


# Now get Headline & description of each drive and the plays of each drive
for drive in DriveList:
    DriveHeadline = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left__Drives__Headline')
    DriveDesc = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left__Drives__Description')
    new_desc = ', '.join((DriveDesc.text).split('\n'))
    print("###",DriveHeadline.text,"->",new_desc)
    PlayList = drive.find_elements(By.CLASS_NAME, 'PlayListItem')
    new_string = ', '.join((drive.text).split('\n'))
    # print("##",new_string)
    for play in PlayList:
        new_string = ', '.join((play.text).split('\n'))
        print("#",play.text)

'''
'''
try:
    PlayList = driver.find_elements(By.CLASS_NAME, 'PlayListItem')
except NoSuchElementException:
    # ??? exception is not correctly handled ???
    print("No such element")

for play in PlayList:
    print(play.text)


if exception == True:
    print("EXCEPTION WAS HANDLED:  DATA IS INCOMPLETE")


time.sleep(10) # Sleep for 3 seconds


driver.quit()


