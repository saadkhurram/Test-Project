
import logging
import sys
from googleSearch import search_google,go_to_images
from innitials import Driverclass

import logging
logger = logging.getLogger()

myDriver = Driverclass()

def test_google_searchall():
    search_google(myDriver.driver, 'test')



def test_image_search():
    result = go_to_images(myDriver.driver)
    assert result == "Pass"



# search_google(myDriver.driver, 'test')
# go_to_images(myDriver.driver)

myDriver.closedriver()



