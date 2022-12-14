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
   us = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Email']")
   us.send_keys("patric@devaxcel.com")

   time.sleep(1)
   pa = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Password']")
   pa.send_keys("1Qazxsw2@")

   time.sleep(1)
   btn = driver.find_element(By.XPATH, "//button[@type = 'submit']")
   btn.click()

   time.sleep(10)
   link = driver.current_url
   print("The current url is:" + str(link))
   if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
      print(" A status is: LOGIN SUCCESSFUL")
   else:
      msg = driver.find_element(By.XPATH, "//div[@class='row justify-center q-pt-sm q-pb-md']").text
      print(msg)
      if "Please verify your email" in msg:
         print(" A status is: LOGIN NOT SUCCESS")

def signupCPA(): #create the exact user

   # to select the button
   time.sleep(10)
   btn = driver.find_elements(By.TAG_NAME, "b")
   print(len(btn))
   print("btn is" ,btn[3].text)
   btnclick = btn[3]
   btnclick.click()

   # to enter the details in signup screen

   time.sleep(2)
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

   time.sleep(4)
   privacy = driver.find_elements(By.XPATH, "//div[@class='q-checkbox__bg absolute']")
   print(len(privacy))

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
   mail.send_keys("sw10.auto@devaxcel.com")

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


   time.sleep(20)
   link=driver.current_url
   print("The current url is:" + str(link))
   if link == "https://dev.eminusgroup.com/#/emailVerification":
      print(" A status is: USER CREATED SUCCESSFUL")
   else:
      createbtn = driver.find_element(By.XPATH, "//button[@type='button']")
      createbtn.click()
      time.sleep(4)
      msg = driver.find_element(By.XPATH, "//div[@class='q-notifications']").text
      print(msg)
      if "Already Registered User" in msg:
         print("mail check completed")
      else:
         print("other issues")

def ClientCheck():



   time.sleep(4)
   addclient = driver.find_elements(By.TAG_NAME, "i")
   print("i tag length:", len(addclient))
   addclient[4].click()

   time.sleep(4)
   companyname = driver.find_elements(By.XPATH, "//input[@class='q-field__native q-placeholder']")
   print("lenth of textbox:", len(companyname))
   companyname[0].send_keys("autouser8a")  # existing company name

   industry = driver.find_elements(By.XPATH, "//input[@role='combobox']")
   print("length of combobox:", len(industry))
   industryselect = industry[0]
   ActionChains(driver).move_to_element(industryselect).click(industryselect).perform()
   time.sleep(2)
   industryvalue = driver.find_elements(By.CLASS_NAME, "q-item__label")
   print("length of industries:", len(industryvalue))
   industryvalue[4].click()

   state = driver.find_elements(By.XPATH, "//input[@role='combobox']")
   print("lengh of combobox:", len(state))
   stateselect = state[1]
   ActionChains(driver).move_to_element(stateselect).click(stateselect).perform()
   time.sleep(2)
   statevalue = driver.find_elements(By.CLASS_NAME, "q-item__label")
   print("length of states:", len(statevalue))
   statevalue[24].click()

   city = driver.find_elements(By.XPATH, "//input[@role='combobox']")
   print("lengh of combobox:", len(city))
   cityselect = city[2]
   ActionChains(driver).move_to_element(cityselect).click(cityselect).perform()
   time.sleep(1)
   cityvalue = driver.find_elements(By.CLASS_NAME, "q-item__label")
   print("length of cities:", len(cityvalue))
   cityvalue[1].click()

   usd = driver.find_elements(By.XPATH, "//input[@role='combobox']")
   print("lengh of combobox:", len(usd))
   usdselect = usd[3]
   ActionChains(driver).move_to_element(usdselect).click(usdselect).perform()
   time.sleep(1)
   usdvalue = driver.find_elements(By.CLASS_NAME, "q-item__label")
   print("length of usd:", len(usdvalue))
   usdvalue[6].click()

   time.sleep(1)
   name = driver.find_elements(By.XPATH, "//input[@class='q-field__native q-placeholder']")
   print("lenth of textbox:", len(name))
   name[1].send_keys("autotest")

   time.sleep(1)
   position = driver.find_elements(By.XPATH, "//input[@class='q-field__native q-placeholder']")
   print("lenth of textbox:", len(position))
   position[2].send_keys("automanager")

   time.sleep(1)
   email = driver.find_elements(By.XPATH, "//input[@class='q-field__native q-placeholder']")
   print("lenth of textbox:", len(email))
   email[3].send_keys("autouser.6a@devaxcel.com")

   time.sleep(1)
   phno = driver.find_elements(By.XPATH, "//input[@class='q-field__native q-placeholder']")
   print("lenth of textbox:", len(phno))
   phno[4].send_keys("8787654321")

   time.sleep(1)
   submitbtn = driver.find_elements(By.XPATH, "//button[@type='submit']")
   print("length of submit button", len(submitbtn))
   submitbtn[0].click()

   time.sleep(2)
   submitbtn = driver.find_elements(By.XPATH, "//button[@type='button']")
   print(len(submitbtn))
   for btn in submitbtn:
      print(btn.get_attribute('innerHTML'))

   submitbtn[2].click()

   submitbtn = driver.find_elements(By.XPATH, "//button[@type='button']")
   time.sleep(5)
   statement = driver.current_url
   print("current url:", statement)
   if statement == "https://dev.eminusgroup.com/#/app/homeDashboard":
      print("Client created")
   else:
      time.sleep(2)
      card = driver.find_element(By.XPATH, "//div[@class='q-card']")
      print("error message is: ",card.text)


def DataEntryUser():


   driver.implicitly_wait(4)
   btns = driver.find_elements(By.XPATH, "//button[@type='button']")
   print("btns:", len(btns))
   for btn in btns:
      print(btn.text)

   time.sleep(1)
   btns[2].click()

   time.sleep(1)
   tabs = driver.find_elements(By.XPATH, "//div[@role='tab']")
   print("tabs:", len(tabs))
   for tab in tabs:
      print(tab.get_attribute("innerHTML"))

   user = tabs[1]
   user.click()

   addbtn = driver.find_elements(By.XPATH, "//button[@type='button']")
   print("addbtns:", len(addbtn))
   print(addbtn[4].text)
   addbtn[4].click()
   for add in addbtn:
      print(add.get_attribute("innerHTML"))

   textboxeslist = driver.find_elements(By.XPATH, "//input[@type='text']")
   print(len(textboxeslist))

   time.sleep(1)
   print(textboxeslist[1].text)
   for box in textboxeslist:
      print(box.get_attribute("innerHTML"))
   time.sleep(1)
   ActionChains(driver).move_to_element(textboxeslist[0]).click(textboxeslist[0]).perform()
   textboxeslist[1].send_keys("ivana@devaxcel.com")
   textboxeslist[2].send_keys("ivanna")
   textboxeslist[3].send_keys("9090834215")

   time.sleep(1)
   buttons = driver.find_elements(By.XPATH, "//button[@type='submit']")
   print(len(buttons))
   buttons[0].click()
   time.sleep(4)
   msg = driver.find_element(By.XPATH, "//div[@class='q-notifications']").text
   print("A notification msessage is :" + str(msg))


#signupCPA()
emlogin()
#ClientCheck()
DataEntryUser()