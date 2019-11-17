from selenium import webdriver
import chromedriver_binary # adds chromedriver binary to path
from time import sleep
from timetable_functions import * # trusted file


all_classes_by_code = ["KIT","KMA","BMA"]

browser = webdriver.Chrome()
browser.get("https://student-timetable.utas.edu.au/#Search")

sleep(5)

generate_timetable(all_classes_by_code, browser) # create a timetable
scrape_timetable(browser)
next_timetable(browser)
browser.close()
