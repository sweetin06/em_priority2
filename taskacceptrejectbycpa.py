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
    us.send_keys("autotest1@devaxcel.com")

    time.sleep(1)
    pa = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Password']")
    pa.send_keys("2Qazxsw2@")

    time.sleep(1)
    btn = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    btn.click()

    """time.sleep(8)
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        msg = driver.find_element(By.XPATH,"//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(msg)
        if "Please verify your email" in msg:
            print(" A status is: LOGIN NOT SUCCESS")"""

def emcreatetask():

    time.sleep(8)
    btns=driver.find_elements(By.XPATH,"//button[@type='button']")
    print("btns:",len(btns))

    for btn in btns:
        print(btn.get_attribute("innerHTML"))

    time.sleep(1)
    if btns[1].text=="Data Entry":
        btns[1].click()

def emselectfilter():
    time.sleep(2)
    filters = driver.find_elements(By.XPATH, "//input[@role='combobox']")
    print("filters:", len(filters))
    filter = filters[0]
    ActionChains(driver).move_to_element(filter).click(filter).perform()
    time.sleep(2)
    options = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    print("options in filter:", options)
    for option in options:
        if option.text == "In Review":
            option.click()

def emclickviwedata():
    time.sleep(1)
    table=driver.find_element(By.XPATH,"//table[@class='q-table']")
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(table).click(table).perform()
    time.sleep(2)
    viewdatabtns=driver.find_elements(By.XPATH,"//button[@type='button']")
    print(len(viewdatabtns))
    for viewdatabtn in viewdatabtns:
        print(viewdatabtn.get_attribute("innerHTML"))

    if viewdatabtns[4].text=="View Data":
        viewdatabtns[4].click()

#btns[8] is accept
def emaccept():
    driver.implicitly_wait(4)
    revenue = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    revenueselect = revenue[0]
    print("length of fields:", len(revenue))
    ActionChains(driver).move_to_element(revenueselect).click(revenueselect).perform()
    revenuevalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    print("No of data entry fields", len(revenuevalue))
    revenuevalue[0].send_keys(Keys.CONTROL + "a")
    revenuevalue[0].send_keys(Keys.DELETE)
    revenuevalue[0].send_keys("44300")

    time.sleep(2)
    btns=driver.find_elements(By.XPATH,"//button[@type='button']")
    print("btns in data accept page:",len(btns))
    for acceptbtn in btns:
        print(acceptbtn.text)

    if btns[8].text=="Accept":
        driver.execute_script("arguments[0].click()", btns[8])
    else:
        print("Check your code")

    time.sleep(2)
    nottification=driver.find_element(By.XPATH,"//div[@class='q-card']")
    print(nottification.text)

#btns[9]is reject
def emreject():
    driver.implicitly_wait(4)
    revenue = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    revenueselect = revenue[0]
    print("length of fields:", len(revenue))
    ActionChains(driver).move_to_element(revenueselect).click(revenueselect).perform()
    revenuevalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    print("No of data entry fields", len(revenuevalue))
    revenuevalue[0].send_keys(Keys.CONTROL + "a")
    revenuevalue[0].send_keys(Keys.DELETE)
    revenuevalue[0].send_keys("44300")

    time.sleep(2)
    btns=driver.find_elements(By.XPATH,"//button[@type='button']")
    print("btns in data accept page:",len(btns))
    print(btns[9].text)
    for rejectbtn in btns:
        print(rejectbtn.text)

    if btns[9].text=="Reject":
        driver.execute_script("arguments[0].click()", btns[9])
    else:
        print("Check your code")

    time.sleep(3)
    nottification=driver.find_element(By.XPATH,"//div[@class='q-card']")
    print(nottification.text)


emlogin()
emcreatetask()
emselectfilter()
emclickviwedata()
#emaccept()
emreject()