import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://dev.eminusgroup.com/#/")


def emlogincpa():

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

def emloginclient():
   time.sleep(2)
   us = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Email']")
   us.send_keys("patric+1a@devaxcel.com")

   time.sleep(1)
   pa = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Password']")
   pa.send_keys("1Qazxsw2@")

   time.sleep(1)
   btn = driver.find_element(By.XPATH, "//button[@type = 'submit']")
   btn.click()

   time.sleep(8)
   link = driver.current_url
   print("The current url is:" + str(link))
   if link == "https://dev.eminusgroup.com/#/smbDashboard":
       print(" A status is: LOGIN SUCCESSFUL")
   else:
       msg = driver.find_element(By.XPATH, "//div[@class='row justify-center q-pt-sm q-pb-md']").text
       print(msg)
       if "Please verify your email" in msg:
           print(" A status is: LOGIN NOT SUCCESS")

def emdataentryuserlogin():
   time.sleep(2)
   us = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Email']")
   us.send_keys("autotestuser.1@devaxcel.com")

   time.sleep(1)
   pa = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Password']")
   pa.send_keys("1Qazxsw2@")

   time.sleep(1)
   btn = driver.find_element(By.XPATH, "//button[@type = 'submit']")
   btn.click()

   time.sleep(8)
   link = driver.current_url
   print("The current url is:" + str(link))
   if link == "https://dev.eminusgroup.com/#/dataEntryUserDashboard":
       print(" A status is: LOGIN SUCCESSFUL")
   else:
       msg = driver.find_element(By.XPATH, "//div[@class='row justify-center q-pt-sm q-pb-md']").text
       print(msg)
       if "Please verify your email" in msg:
           print(" A status is: LOGIN NOT SUCCESS")


emlogincpa()
#emloginclient()
#emdataentryuserlogin()
