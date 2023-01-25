from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def solarwinds_display_default(driver, url, timer, user, passwd):


    #ob2 = Screenshot_Clipping.Screenshot()

    driver.get(url)
    time.sleep(timer)
    elem = driver.find_element("id", "ctl00_BodyContent_Username")
    elem.send_keys(user)
    elem = driver.find_element("id", "ctl00_BodyContent_Password")
    elem.send_keys(passwd)
    elem = driver.find_element(By.CLASS_NAME, "sw-btn-primary")
    elem.send_keys(Keys.ENTER)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='75%'")
    time.sleep(timer)
    #img_url2 = ob2.full_Screenshot(driver, save_path=path_url, image_name='SolarWindsDashboard.png')
