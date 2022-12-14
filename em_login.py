import time
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException,
                                        NoSuchElementException)

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://dev.eminusgroup.com/#/")

def em__login():
    time.sleep(2)
    us = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Email']")
    us.send_keys("patric@devaxcel.com")

    time.sleep(1)
    pa = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Password']")
    pa.send_keys("1Qazxsw2@")

    time.sleep(1)
    btn = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    btn.click()

    ignore_list = [NoSuchElementException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    element = wait.until(EC.element_to_be_clickable((By.ID, "appHeader_profile_btn")))
    #wait.until(EC.element_to_be_clickable(By.ID, "appHeader_profile_btn"))
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        msg = driver.find_element(By.XPATH,"//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(msg)
        if "Please verify your email" in msg:
            print(" A status is: LOGIN NOT SUCCESS")

em__login()