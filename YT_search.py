from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()  # Initialize the driver with Chrome

    def play(self, query): #main fuction to run youtube video
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)  # opening the youtube website using the Chrome driver
        videos = self.driver.find_elements("id",'video-title')
        videos[0].click()
        while True:
            pass


