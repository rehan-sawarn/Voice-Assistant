from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()  # Initialize the driver with Chrome

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")  # opening the wikipedia website using the Chrome driver
        search = self.driver.find_element("xpath",'//*[@id="searchInput"]') # locating the search bar
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath",'//*[@id="search-form"]/fieldset/button') # locating the search button
        enter.click()
        while True:
            pass