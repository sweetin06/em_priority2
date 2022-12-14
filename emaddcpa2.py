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

def signup1(): #create the exact user

   # to select the button
   time.sleep(5)
   btn = driver.find_elements(By.TAG_NAME, "b")
   print(len(btn))
   print("btn is" ,btn[3].text)
   btnclick = btn[3]
   btnclick.click()


   # to enter the details in signup screen

   time.sleep(5)
   firmname = driver.find_element(By.XPATH,"//input[@placeholder = 'ex. Acme S. A.']")
   firmname.send_keys("cpaauto")

   address = driver.find_element(By.XPATH,"//input[@placeholder = 'Number, Street & State']")
   address.send_keys("india")

   options =  driver.find_elements(By.XPATH,"//input[@aria-label = 'Select a option']")
   print("no of options:",len(options))

   time.sleep(2)
   partners = driver.find_elements(By.XPATH,"//input[@aria-label='Select a option']")[0]
   driver.implicitly_wait(2)
   ActionChains(driver).move_to_element(partners).click(partners).perform()
   partnerselect = driver.find_elements(By.CLASS_NAME,"q-item__label")
   print("list of partners",len(partnerselect))
   time.sleep(2)
   for partnerclick in partnerselect:
       partnerclick = partnerselect[4]
       partnerclick.click()

   time.sleep(2)
   clients = driver.find_elements(By.XPATH,"//input[@aria-label='Select a option']")[1]
   driver.implicitly_wait(2)
   ActionChains(driver).move_to_element(clients).click(clients).perform()
   clientselect = driver.find_elements(By.CLASS_NAME,"q-item__label")
   print("list of clients",len(clientselect))
   time.sleep(2)
   for clientclick in clientselect:
       clientclick = clientselect[1]
       clientclick.click()

   time.sleep(2)
   offices = driver.find_elements(By.XPATH,"//input[@aria-label='Select a option']")[2]
   driver.implicitly_wait(2)
   ActionChains(driver).move_to_element(offices).click(offices).perform()
   officeselect = driver.find_elements(By.CLASS_NAME,"q-item__label")
   print("list of offices",len(officeselect))
   time.sleep(2)
   for officeclick in officeselect:
       officeclick = officeselect[1]
       officeclick.click()


   tab = driver.find_elements(By.XPATH,"//form[@class='q-form']")
   print("no of tabs:", len(tab))

   """for ta in tab:
       print(ta.get_attribute("innerHTML"))"""

   time.sleep(2)
   tab = driver.find_elements(By.XPATH,"//form[@class='q-form']")[1]
   driver.implicitly_wait(2)
   #ActionChains(tab).move_to_element(tab).perform()

   time.sleep(2)
   firstname = driver.find_element(By.XPATH,"//input[@placeholder='ex.Jean ']")
   firstname.send_keys("automation")

   time.sleep(1)
   lastname = driver.find_element(By.XPATH,"//input[@placeholder='ex.Massad']")
   lastname.send_keys("testing")

   time.sleep(1)
   mail = driver.find_element(By.XPATH,"//input[@placeholder='example@email.com']")
   mail.send_keys("sw17.auto@devaxcel.com")

   time.sleep(1)
   phno = driver.find_element(By.XPATH,"//input[@placeholder='(307) 555-0133']")
   phno.send_keys("1234123028")

   states = driver.find_elements(By.XPATH,"//input[@aria-label='Select a option']")[3]
   driver.implicitly_wait(2)
   ActionChains(driver).move_to_element(states).click(states).perform()
   state = driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
   print("state",len(state))
   time.sleep(2)
   stateclick = state[15]
   stateclick.click()

   time.sleep(4)
   privacy = driver.find_elements(By.XPATH, "//div[@class='q-checkbox__bg absolute']")
   print(len(privacy))
   privacy[0].click()

   time.sleep(2)
   createbtn = driver.find_element(By.XPATH,"//button[@type='button']")
   createbtn.click()

   time.sleep(10)
   link=driver.current_url
   print("The current url is:" + str(link))
   if link == "https://dev.eminusgroup.com/#/emailVerification":
      print(" A status is: USER CREATED SUCCESSFUL")
   else:
      msg = driver.find_element(By.XPATH, "//div[@class='q-notifications']").text
      print("A notification msessage is :" + str(msg))
      if "privacy" in msg:
         print("Terms of condition is not selected")
      elif "Already" in msg:
         print("A already registered mail id entered")
      else:
         time.sleep(2)
         errmsg = driver.find_elements(By.XPATH, "//div[@class='q-field__messages col']")
         print("length of error message", len(errmsg))
         for er in errmsg:
            print(er.text)
signup1()