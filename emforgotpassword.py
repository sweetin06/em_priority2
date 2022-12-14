import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException,
                                        NoSuchElementException, StaleElementReferenceException,
                                        ElementNotInteractableException)



options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://dev.eminusgroup.com/#/")

def forgot_password():

    time.sleep(2)
    options=driver.find_elements(By.CLASS_NAME,"cursor-pointer")
    print("Length of options in sign in page:",len(options))
    for forgotoption in options:
        if forgotoption.text=="Forgot Password":
            forgotoption.click()

    ignore_list = [NoSuchElementException, ElementNotSelectableException,StaleElementReferenceException,ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))

    driver.implicitly_wait(2)
    email=driver.find_element(By.XPATH,"//input[@aria-label='email']")
    email.send_keys("autotestuser.1@devaxcel.com")

    time.sleep(1)
    nextbutton = driver.find_element(By.XPATH,"//button[@type='submit']")
    nextbutton.click()

    time.sleep(2)


    notification = driver.find_element(By.XPATH, "//div[@class='q-notification__message col']")
    print("A notification message is:",notification.text)

forgot_password()