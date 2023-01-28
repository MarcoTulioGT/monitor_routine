from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from screenshot import take_screenshot

def solarwinds_display_default(driver, url, timer, user, passwd,screen):



    driver.get(url)
    time.sleep(timer)
    elem = driver.find_element("id", "ctl00_BodyContent_Username")
    elem.send_keys(user)
    elem = driver.find_element("id", "ctl00_BodyContent_Password")
    elem.send_keys(passwd)
    elem = driver.find_element(By.CLASS_NAME, "sw-btn-primary")
    elem.send_keys(Keys.ENTER)
    #driver.maximize_window()
    driver.execute_script("document.body.style.zoom='75%'")
    time.sleep(timer)

    #take a full screen
    take_screenshot(driver, screen)
