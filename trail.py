import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import logging


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

    time.sleep(10)
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        msg = driver.find_element(By.XPATH,"//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(msg)
        if "Please verify your email" in msg:
            print(" A status is: LOGIN NOT SUCCESS")

    print("______________________________________________________")


def emaddclient():

    time.sleep(6)
    buttons=driver.find_elements(By.XPATH,"//button[@type='button']")
    print("Buttons length in home dashboard:",len(buttons))
    print(type(buttons))
    print(buttons[0].text)
    print(type(buttons[0]))
    for button in buttons:
        print(button.text)

    print("_________________________________________")
    print("Text of button[4]",)
    print(buttons[4].text)

    #buttons[4].click()

    if buttons[4].text=="add\nAdd Client":
        print("TEXT MATCHED")
        buttons[4].click()
    else:
        print("TEXT MIS-MATCHED")


emlogin()
emaddclient()