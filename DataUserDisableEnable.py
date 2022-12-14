import time
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://dev.eminusgroup.com/#/")


def emlogin():

    time.sleep(2)
    us = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Email']")
    us.send_keys("patric@devaxcel.com")

    time.sleep(1)
    pa = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Password']")
    pa.send_keys("1Qazxsw2@")

    time.sleep(1)
    btn = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    btn.click()

    time.sleep(8)
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        msg = driver.find_element(By.XPATH,"//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(msg)
        if "Please verify your email" in msg:
            print(" A status is: LOGIN NOT SUCCESS")

def emcreatetask():
    btns=driver.find_elements(By.XPATH,"//button[@type='button']")
    print("btns:",len(btns))
    for btn in btns:
        print(btn.get_attribute("innerHTML"))

    time.sleep(1)
    btns[2].click()

    time.sleep(3)
    tabs=driver.find_elements(By.XPATH,"//div[@role='tab']")
    print("tabs:",len(tabs))
    for tab in tabs:
        print(tab.get_attribute("innerHTML"))
    time.sleep(1)
    tabs[1].click()

    driver.implicitly_wait(4)
    toggles=driver.find_elements(By.XPATH,"//div[@class='q-toggle__track']")
    print(len(toggles))
    for tog in toggles:
        print(tog.get_attribute("innerHTML"))

    time.sleep(2)
    driver.execute_script("arguments[0].click()",toggles[0])

    time.sleep(2)
    popupmsg=driver.find_element(By.XPATH,"//div[@class='q-card']")
    ActionChains(driver).move_to_element(popupmsg).click(popupmsg).perform()
    okbtn=driver.find_elements(By.XPATH,"//button[@type='button']")
    for ok in okbtn:
        if ok.text=="OK":
            ok.click()


emlogin()
emcreatetask()