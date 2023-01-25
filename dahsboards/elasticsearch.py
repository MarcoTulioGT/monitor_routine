from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def elastic_display_default(driver, url, timer, user, passwd):

    #ob = Screenshot_Clipping.Screenshot()
    ##driver = webdriver.Chrome(DRIVER)
    driver.get(url)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='65%'")
    time.sleep(timer/2)
    elem = driver.find_element("name", "username")
    elem.send_keys(user)
    elem = driver.find_element("name", "password")
    elem.send_keys(passwd)
    elem = driver.find_element(By.CLASS_NAME,"euiButton--primary")
    elem.send_keys(Keys.ENTER)
    time.sleep(timer)
    #img_url = ob.full_Screenshot(driver, save_path= path_url, image_name='URL_SSITDashboard.png')

