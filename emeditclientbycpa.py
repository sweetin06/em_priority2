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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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

    """driver.implicitly_wait(10)
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        msg = driver.find_element(By.XPATH,"//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(msg)
        if "Please verify your email" in msg:
            print(" A status is: LOGIN NOT SUCCESS")"""


def emselectmenu():

    time.sleep(10)
    tags=driver.find_elements(By.XPATH,"//button[@dropdownicon='more_vert']")
    print("tags:",len(tags))
    for tag in tags:
        print(tag.get_attribute("innerHTML"))

    time.sleep(2)
    tag0=tags[0]
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(tag0).click(tag0).perform()
    editoption=driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
    print("options",len(editoption))
    editoption[2].click()

def emclientediting():

    time.sleep(3)
    textboxes=driver.find_elements(By.XPATH,"//input[@type='text']")
    print("textboxes:",len(textboxes))

    time.sleep(1)
    comboboxes=driver.find_elements(By.XPATH,"//input[@role='combobox']")
    print("comboboxes",len(comboboxes))

    time.sleep(1)
    companyname = textboxes[0]
    companyname.send_keys(Keys.CONTROL + "a")
    companyname.send_keys(Keys.DELETE)
    companyname.send_keys("autotesting128")

    industry = comboboxes[0]
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(industry).click(industry).perform()
    industryselect = driver.find_elements(By.CLASS_NAME, "q-item__label")
    print("industries", len(industryselect))
    time.sleep(1)
    industryselect[4].click()

    states = comboboxes[1]
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(states).click(states).perform()
    stateselect = driver.find_elements(By.CLASS_NAME, "q-item__label")
    print("states", len(stateselect))
    time.sleep(1)
    stateselect[17].click()

    city = comboboxes[2]
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(city).click(city).perform()
    cityselect = driver.find_elements(By.CLASS_NAME, "q-item__label")
    print("cities:", len(cityselect))
    time.sleep(1)
    cityselect[1].click()

    time.sleep(1)
    name = textboxes[1]
    name.send_keys(Keys.CONTROL + "a")
    name.send_keys(Keys.DELETE)
    name.send_keys("automation")

    time.sleep(1)
    position = textboxes[2]
    position.send_keys(Keys.CONTROL + "a")
    position.send_keys(Keys.DELETE)
    position.send_keys("tester")

    # textboxes3 is email field not editable

    time.sleep(1)
    phno = textboxes[4]
    phno.send_keys(Keys.CONTROL + "a")
    phno.send_keys(Keys.DELETE)
    phno.send_keys("6767676767")

    time.sleep(2)
    btn=driver.find_elements(By.XPATH,"//button[@type='submit']")
    print(len(btn))
    btn[0].click()

    time.sleep(2)
    card = driver.find_elements(By.XPATH, "//div[@class='q-card']")
    print(card[0].text)

    time.sleep(2)
    editdata=driver.find_elements(By.XPATH,"//div[@class='q-stepper__title']")
    print(len(editdata))


emlogin()
emselectmenu()
emclientediting()
