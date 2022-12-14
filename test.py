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

    taskbtns=driver.find_elements(By.XPATH,"//button[@type='button']")
    print("length of buttons",len(taskbtns))
    for task in taskbtns:
        print(task.get_attribute("innerHTML"))
    taskbtns[3].click()

    #selecting a year btn
    years=driver.find_elements(By.XPATH,"//button[@type='button']")
    print("years",len(years))
    for year in years:
        print(year.get_attribute("innerHTML"))
    driver.execute_script("arguments[0].click()", years[5])

    #selecting a year
    yearselect = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    for year in yearselect:
        if year.text == "2020":
            year.click()

    time.sleep(2)
    quarterselect = driver.find_elements(By.XPATH, "//input[@type='radio']")
    # ActionChains(driver).move_to_element(quarterselect).perform()
    print(len(quarterselect))
    quarters = driver.find_elements(By.XPATH, "//div[@class='q-radio__label q-anchor--skip']")
    for quarter in quarters:
        if quarter.text == "Third Quarter":
            quarter.click()


    time.sleep(2)
    years[5].click()

    time.sleep(1)
    comboboxes = driver.find_elements(By.XPATH, "//div[@class='q-field__native row items-center']")
    print("comboboxes", len(comboboxes))

    time.sleep(1)
    emails = comboboxes[1]
    ActionChains(driver).move_to_element(emails).click(emails).perform()
    emaillist = driver.find_elements(By.CLASS_NAME,"q-item__label")
    print("emaillist",len(emaillist))
    for email in emaillist:
        if email.text == "swee@devaxcel.com":
            time.sleep(1)
            email.click()

    time.sleep(1)
    orgname=comboboxes[2]
    ActionChains(driver).move_to_element(orgname).click(orgname).perform()
    time.sleep(1)
    orgnamelist=driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    for org in orgnamelist:
        if org.text == "autotest":
            org.click()

    """time.sleep(1)
    taskbtns=driver.find_elements(By.XPATH,"//button[@type='button']")
    print(len(taskbtns))
    print(taskbtns[7].text)
    taskbtns[7].click()

    time.sleep(1)
    msg = driver.find_element(By.XPATH, "//div[@class='q-notifications']").text
    print("A notification msessage is :" + str(msg))"""



emlogin()
emcreatetask()