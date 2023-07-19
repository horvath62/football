
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException, TimeoutException, ElementClickInterceptedException

import time

class scrape:
    def __init__(self):
        self.rawplaylist = []

    def scrapeplays(self, gameID, wait_time):
        exception = False

        driver = webdriver.Chrome()

        # driver.get('https://scrapingclub.com/')
        URL = 'https://www.espn.com/college-football/playbyplay/_/gameId/' + str(gameID)
        driver.get( URL )

        # delay to let page load
        time.sleep(wait_time) # Sleep

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
        time.sleep(wait_time)


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
            time.sleep(wait_time)

        # Now get Headline & description of each drive and the plays of each drive
        for drive in DriveList:
            DriveHeadline = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left__Drives__Headline')
            DriveDesc = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Left__Drives__Description')
            DriveScore = drive.find_element(By.CLASS_NAME, 'AccordionHeader__Right')
            new_headline = "# " + DriveHeadline.text
            new_headline = new_headline + ', ' + ', '.join((DriveDesc.text).split('\n'))
            new_headline = new_headline + ', ' + ', '.join((DriveScore.text).split('\n'))
            print(new_headline)
            self.rawplaylist.append(new_headline)

            PlayList = drive.find_elements(By.CLASS_NAME, 'PlayListItem')
            for play in PlayList:
                new_play = ' '.join((play.text).split('\n'))
                print(new_play)
                self.rawplaylist.append(new_play)

        if exception:
            print("EXCEPTION WAS HANDLED:  DATA IS INCOMPLETE")

        driver.quit()

        return exception
