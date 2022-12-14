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
    us.send_keys("bc@devaxcel.com")

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
    btns[1].click()

    time.sleep(1)
    tabs=driver.find_elements(By.XPATH,"//div[@role='tab']")
    print("tabs:",len(tabs))
    for tab in tabs:
        print(tab.get_attribute("innerHTML"))
    time.sleep(1)
    tabs[0].click()


def emusersearch():
    searchbtn=driver.find_element(By.XPATH,"//input[@aria-label='Search']")
    a="testa"
    searchbtn.send_keys(a)
    #print("searchbtns:",len(searchbtns))

    values=driver.find_elements(By.XPATH,"//div[@class='task-text table-color']")
    for value in values:
        print(value.text)
        if value.text=='testa':
            print("A value selected")
        else:
            print("something went wrong")

def emselectfilter():
   filters=driver.find_elements(By.XPATH,"//input[@role='combobox']")
   print("filters:",len(filters))
   filter=filters[0]
   ActionChains(driver).move_to_element(filter).click(filter).perform()
   time.sleep(2)
   options=driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
   print("options in filter:",options)
   for option in options:
       if option.text=="Created":
           option.click()

   time.sleep(1)
   statustext=driver.find_elements(By.XPATH,"//div[@role='alert']")
   print("status text:",len(statustext))
   for status in statustext:
       if status.text=="Created":
           print("Created is selected")
       else:
           print("Something went wrong")
def emfilters():
    searchbtn = driver.find_element(By.XPATH, "//input[@aria-label='Search']")
    a = "testa"
    searchbtn.send_keys(a)

    time.sleep(2)
    filters = driver.find_elements(By.XPATH, "//input[@role='combobox']")
    print("filters:", len(filters))
    filter = filters[0]
    ActionChains(driver).move_to_element(filter).click(filter).perform()
    time.sleep(2)
    options = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    print("options in filter:", len(options))
    for option in options:
        if option.text == "Created":
            option.click()

    time.sleep(2)
    values = driver.find_elements(By.XPATH, "//div[@class='task-text table-color']")
    print("searched things", len(values))
    for a in values:
        print(a.text)

    time.sleep(1)
    statustext = driver.find_elements(By.XPATH, "//div[@role='alert']")
    print("status text:", len(statustext))



emlogin()
emcreatetask()
#emusersearch()
#emselectfilter()
emfilters()