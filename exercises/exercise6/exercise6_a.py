from userinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def singIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        username = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")

