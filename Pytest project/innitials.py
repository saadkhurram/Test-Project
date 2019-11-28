import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
logger.addHandler(stream)



# class Logger:
#     def createlogger(self):
#         # Logger Code
#         self.logger = logging.getLogger('Persivia Add Patient')
#         self.logger.setLevel(logging.DEBUG)
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         # create formatter
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         # add formatter to ch
#         ch.setFormatter(formatter)
#         # add ch to logger
#         self.logger.addHandler(ch)
#         return self.logger


class Driverclass:
    chromePrefs = {"profile.default_content_setting_values.notifications": 2,
                   "profile.default_content_settings.popups": 0}
    chromedriver = "D:\\chromedriver"

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", self.chromePrefs)
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(self.chromedriver, chrome_options=options)
        logger.info("Chrome browser opened ")
        action = ActionChains(self.driver)
        action.key_down(Keys.SHIFT).key_down(Keys.CONTROL).key_down('N')
        logger.info("incognoto window opened")
        self.driver.maximize_window()
        logger.info("Window is maximized")
        options = webdriver.ChromeOptions()

    # def getdriver(self):

    def closedriver(self):
        self.driver.close()
        self.driver.quit()


