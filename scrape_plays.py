
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException, TimeoutException, ElementClickInterceptedException

import time

def scrapeplays(gameID):
    exception = False

    driver = webdriver.Chrome()

    # driver.get('https://scrapingclub.com/')
    URL = 'https://www.espn.com/college-football/playbyplay/_/gameId/' + str(gameID)
    driver.get( URL )

    # delay to let page load
    time.sleep(0.5) # Sleep

    # Collapse first drive playlist (because it default is expanded, remaining playlists are collapsed)
    try:
        DriveFirst = driver.find_element(By.CLASS_NAME, "AccordionPanel.Panel")
        D1 = DriveFirst.find_element(By.CLASS_NAME, 'AccordionHeader__Left')
        R1 = DriveFirst.find_element(By.CLASS_NAME, 'AccordionHeader__Right')
        D1.click()
        R1.click()
    except NoSuchElementException:
        print("Exception: No Such Element")
        exception = True
    except ElementClickInterceptedException:
        print("Exception: Element Click Intercepted")
        exception = True
    time.sleep(0.5)


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
            driveScore = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Right')
            driveHeader.click()
        except NoSuchElementException:
            print("Exception: No Such Element")
            exception = True
        except ElementClickInterceptedException:
            print("Exception: Element Click Intercepted")
            print("Try increasing sleep time between clicks to allow html page to re-render")
            exception = True
        time.sleep(0.2)
        print("##", drive.text)

    # Now get Headline & description of each drive and the plays of each drive
    for drive in DriveList:
        DriveHeadline = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left__Drives__Headline')
        DriveDesc = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left__Drives__Description')
        DriveScore = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Right')
        new_desc = ', '.join((DriveDesc.text).split('\n'))
        new_score = ', '.join((DriveScore.text).split('\n'))
        print("#",DriveHeadline.text,"->",new_desc,new_score)
        PlayList = drive.find_elements(By.CLASS_NAME, 'PlayListItem')
        new_string = ', '.join((drive.text).split('\n'))
        # print("##",new_string)
        for play in PlayList:
            new_play = ' # '.join((play.text).split('\n'))
            print(">",new_play)

    if exception:
        print("EXCEPTION WAS HANDLED:  DATA IS INCOMPLETE")

    driver.quit()

    return exception
