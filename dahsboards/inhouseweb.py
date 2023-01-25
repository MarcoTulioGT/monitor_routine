from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def inhouseweb_display_default(driver, url, timer):


    driver.get(url)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='65%'")
    time.sleep(timer)
    elem = driver.find_element(By.XPATH, "//div[@class= 'sidebar col-xs']/div[6]")
    #elem.send_keys(Keys.ENTER)
    time.sleep(timer)
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(timer/2)
    elem = driver.find_element(By.XPATH, "//div[text()='Weekly']")
    time.sleep(timer)
    driver.execute_script("arguments[0].click();", elem)
    time.sleep(timer)
