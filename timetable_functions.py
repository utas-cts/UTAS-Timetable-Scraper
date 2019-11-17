from time import sleep
from selenium.webdriver.common.keys import Keys # to input to fields

def generate_timetable(unit_codes, browser):
    sleep(3)

    LOCATION_SEARCH_FIELD = browser.find_element_by_xpath(
        '//*[@id="Search"]/div/div[2]/form/div[6]/div/span/span[1]/span/ul/li/input'
    )
    LOCATION_SEARCH_FIELD.send_keys("Launceston")
    LOCATION_SEARCH_FIELD.send_keys(Keys.RETURN)
    sleep(3)
    UNIT_SEARCH_FIELD = browser.find_element_by_xpath(
        '//*[@id="Search"]/div/div[2]/form/div[3]/div/span/span[1]/span/ul/li/input'
    )
    UNIT_SEARCH_FIELD.click()
    
    sleep(2)
    for code in unit_codes:
        UNIT_SEARCH_FIELD.send_keys(code + "*")
        sleep(3)
    # search for and click the search button
    browser.find_element_by_xpath(
        '//*[@id="btnSearch"]'
    ).click()

    #SUBMIT_BUTTON.click()

def scrape_timetable(browser):
    return

def scrape_event(browser):
    # clicking on a card in the timetable brings up more information
    return

def next_timetable(browser):
    sleep(4)
    BACK_BUTTON = browser.find_element_by_xpath(
        '//*[@id="calendar"]/div[1]/div[1]/div[2]/button[1]/span'
    )
    FORWARD_BUTTON = browser.find_element_by_xpath(
        '//*[@id="calendar"]/div[1]/div[1]/div[2]/button[2]/span'
    )
    sleep(2)
    FORWARD_BUTTON.click()
    sleep(2)
