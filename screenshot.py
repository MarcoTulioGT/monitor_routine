from Screenshot import Screenshot

def take_screenshot(driver, name):
    screen = Screenshot.Screenshot()
    screen.full_Screenshot(driver, save_path=r'./images', image_name=name)