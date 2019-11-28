from selenium.webdriver.common.keys import Keys
import sys

import logging

logger = logging.getLogger()


def search_google(my_driver, value):
    try:
        my_driver.get("https://www.google.com")
        my_driver.find_element_by_name('q').send_keys(value)
        my_driver.find_element_by_name('q').send_keys(Keys.RETURN)
        logger.info("search performed")

    except:
        print("search is not performed")


def go_to_images(my_driver):
    try:
        # import pdb; pdb.set_trace()
        my_driver.find_element_by_xpath('//a[@class="q qs"]').click()
        logger.info("Image button found")
        return "Pass"

    except:
        logger.info("Image button not found")
