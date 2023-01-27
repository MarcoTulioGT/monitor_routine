from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from screenshot import take_screenshot

def grafana_display_default(driver, url, timer, user , passwd, screen):
    
    driver.get(url)
    elem = driver.find_element("name", "username")
    elem.send_keys(user)
    elem = driver.find_element("name", "password")
    elem.send_keys(passwd)
    elem = driver.find_element(By.CLASS_NAME,"btn-primary")
    elem.send_keys(Keys.ENTER)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(timer)
    
    #take a full screen
    take_screenshot(driver, screen)
    