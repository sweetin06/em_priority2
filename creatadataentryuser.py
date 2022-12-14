import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


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

def emcreatedataentryuser():
    driver.implicitly_wait(4)
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

    user=tabs[1]
    user.click()

    addbtn=driver.find_elements(By.XPATH,"//button[@type='button']")
    print("addbtns:",len(addbtn))
    print(addbtn[3].text)
    addbtn[3].click()
    for add in addbtn:
        print(add.get_attribute("innerHTML"))

    textboxeslist=driver.find_elements(By.XPATH,"//input[@type='text']")
    print(len(textboxeslist))

    time.sleep(1)
    print(textboxeslist[1].text)
    for box in textboxeslist:
        print(box.get_attribute("innerHTML"))
    time.sleep(1)
    ActionChains(driver).move_to_element(textboxeslist[0]).click(textboxeslist[0]).perform()
    textboxeslist[1].send_keys("dataentryuser.test2@devaxcel.com")
    textboxeslist[2].send_keys("test datauser")
    textboxeslist[3].send_keys("9090834215")

    time.sleep(1)
    buttons=driver.find_elements(By.XPATH,"//button[@type='submit']")
    print(len(buttons))
    buttons[0].click()
    time.sleep(4)
    msg = driver.find_element(By.XPATH, "//div[@class='q-notifications']").text
    print("A notification msessage is :" + str(msg))


emlogin()
emcreatedataentryuser()