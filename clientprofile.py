import time
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException,
                                        NoSuchElementException, TimeoutException)


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://dev.eminusgroup.com/#/")

def emclientlogin():

  time.sleep(2)
  username = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Email']")
  username.send_keys("patric+1a@devaxcel.com")

  time.sleep(1)
  password = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Password']")
  password.send_keys("1Qazxsw2@")

  time.sleep(1)
  signin_btn = driver.find_element(By.XPATH,"//button[@type = 'submit']")
  signin_btn.click()

  ignore_list = [NoSuchElementException, ElementNotSelectableException,TimeoutException]
  wait = WebDriverWait(driver, timeout=20, poll_frequency=1, ignored_exceptions=ignore_list)
  element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
  link = driver.current_url
  print("The current url is:" + str(link))
  if link == "https://dev.eminusgroup.com/#/smbDashboard":
      print(" A status is: LOGIN SUCCESSFUL")
  else:
      msg = driver.find_element(By.XPATH,"//div[@class='row justify-center q-pt-sm q-pb-md']").text
      print(msg)
      if "Please verify your email" in msg:
          print(" A status is: LOGIN NOT SUCCESS")

def emmenubar():
  time.sleep(1)
  menu_bar=driver.find_elements(By.TAG_NAME,"i")
  print(len(menu_bar))
  print("Text of clicking menu item:",menu_bar[1].text)
  driver.execute_script("arguments[0].click()",menu_bar[1])
  time.sleep(1)
  menu_items=driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
  for my_profile in menu_items:
    if my_profile.text=="My Profile":
      driver.execute_script("arguments[0].click()",my_profile)

  print("______")

def emeditprofile():

  driver.implicitly_wait(2)
  ignore_list = [NoSuchElementException, ElementNotSelectableException, TimeoutException]
  wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
  element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']")))
  driver.implicitly_wait(2)
  tab=driver.find_elements(By.XPATH,"//form[@class='q-form row q-mt-lg']")
  ActionChains(driver).move_to_element(tab[0]).click(tab[0]).perform()
  buttons = driver.find_elements(By.XPATH, "//button[@type='button']")
  driver.implicitly_wait(2)
  print("Count of buttons in client profile :", len(buttons))
  for edit_btn in buttons:
    if edit_btn.text=="Edit Information":
      driver.execute_script("arguments[0].click()",edit_btn)


  textboxes = driver.find_elements(By.XPATH,"//input[@type='text']")
  print("length of textboxes",len(textboxes))

  comboboxes = driver.find_elements(By.XPATH, "//input[@role='combobox']")
  print("length of comboboxes", len(comboboxes))

  time.sleep(2)
  company_name=textboxes[0]
  company_name.send_keys(Keys.CONTROL+"a")
  company_name.send_keys(Keys.DELETE)
  company_name.send_keys("autotesting")

  industries=comboboxes[0]
  ActionChains(driver).move_to_element(industries).click(industries).perform()
  industry_items=driver.find_elements(By.CLASS_NAME,"q-item__label")
  time.sleep(1)
  for industry in industry_items:
    if industry.text=="Finance":
      industry.click()
      break


  states=comboboxes[1]
  driver.implicitly_wait(2)
  ActionChains(driver).move_to_element(states).click(states).perform()
  state_select=driver.find_elements(By.CLASS_NAME,"q-item__label")
  print("states",len(state_select))
  time.sleep(1)
  for state in state_select:
    if state.text=="Delaware":
      state.click()
      break



  cities=comboboxes[2]
  driver.implicitly_wait(2)
  ActionChains(driver).move_to_element(cities).click(cities).perform()
  city_select=driver.find_elements(By.CLASS_NAME,"q-item__label")
  print("cities:",len(city_select))
  time.sleep(1)
  for city in city_select:
    if city.text=="Raleigh":
      city.click()
      break


  time.sleep(1)
  name=textboxes[1]
  name.send_keys(Keys.CONTROL+"a")
  name.send_keys(Keys.DELETE)
  name.send_keys("automation")

  time.sleep(1)
  position=textboxes[2]
  position.send_keys(Keys.CONTROL+"a")
  position.send_keys(Keys.DELETE)
  position.send_keys("tester")

  #textboxes3 is email field not editable

  time.sleep(1)
  phone_no=textboxes[4]
  phone_no.send_keys(Keys.CONTROL+"a")
  phone_no.send_keys(Keys.DELETE)
  phone_no.send_keys("6767676767")

  save_btn=driver.find_element(By.XPATH,"//button[@type='submit']")
  if save_btn.text=="Save Changes":
    driver.execute_script("arguments[0].click()",save_btn)

  time.sleep(2)
  message_card=driver.find_element(By.XPATH,"//div[@class='q-card']")
  print(message_card.text)

emclientlogin()
emmenubar()
emeditprofile()
