import time
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException,
                                        NoSuchElementException, TimeoutException)

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://dev.eminusgroup.com/#/")


def em_login():

    time.sleep(2)
    username = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Email']")
    username.send_keys("dataentryuser.testa@devaxcel.com")

    time.sleep(1)
    password = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Password']")
    password.send_keys("1Qazxsw2@")

    time.sleep(1)
    signin_btn = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    signin_btn.click()

    ignore_list = [NoSuchElementException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=20, poll_frequency=1, ignored_exceptions=ignore_list)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']")))

    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/dataEntryUserDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        error_nottification = driver.find_element(By.XPATH, "//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(error_nottification)
        if "Please verify your email" in error_nottification:
            print(" A status is: LOGIN NOT SUCCESS")

def user_profile():

    driver.implicitly_wait(2)
    menubar=driver.find_elements(By.XPATH,"//button[@type='button']")
    driver.execute_script("arguments[0].click()",menubar[2])

    time.sleep(1)
    menuitems=driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
    for edit_menu in menuitems:
        if edit_menu.text=="My Profile":
            edit_menu.click()

    ignore_list = [NoSuchElementException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=20, poll_frequency=1, ignored_exceptions=ignore_list)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))


    forms=driver.find_elements(By.XPATH,"//form[@class='q-form']")
    ActionChains(driver).move_to_element(forms[0]).click(forms[0]).perform()
    time.sleep(1)
    edit_btn_list=driver.find_elements(By.XPATH,"//button[@type='submit']")
    for edit_btn in edit_btn_list:
        if edit_btn.text=="Edit Information":
            edit_btn.click()

    time.sleep(1)
    textboxes=driver.find_elements(By.XPATH,"//input[@type='text']")
    print("Length of textboxes:",len(textboxes))

    name=textboxes[0]
    ActionChains(driver).move_to_element(name).click(name).perform()
    name.send_keys(Keys.CONTROL+"a")
    name.send_keys(Keys.DELETE)
    name.send_keys("name edit")

    time.sleep(1)
    phno=textboxes[2]
    phno.send_keys(Keys.CONTROL+"a")
    phno.send_keys(Keys.DELETE)
    phno.send_keys("3333302222")

    time.sleep(1)
    save_btns_list=driver.find_elements(By.XPATH,"//button[@type='submit']")
    for save_btn in  save_btns_list:
        if save_btn.text=="Save Changes":
            save_btn.click()

    time.sleep(1)
    notification = driver.find_element(By.XPATH, "//div[@class='q-notifications']")
    print(notification.text)


em_login()
user_profile()