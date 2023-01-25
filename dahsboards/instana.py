from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def instana_display_default(driver, url, timer, user, passwd):
    driver.get(url)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='65%'")
    time.sleep(timer/2)
    elem = driver.find_element("name", "email")
    elem.send_keys(user)
    elem = driver.find_element("name", "password")
    elem.send_keys(passwd)
    elem = driver.find_element(By.CLASS_NAME,"in-button")
    elem.send_keys(Keys.ENTER)
    time.sleep(timer)
