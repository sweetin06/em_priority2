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
                                       NoSuchElementException, StaleElementReferenceException)

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# get the url
driver.get("https://dev.eminusgroup.com/#/")


def em_login():
   time.sleep(5)
   username = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Email']")
   username.send_keys("eminusadmin11@devaxcel.com")

   time.sleep(1)
   password = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Password']")
   password.send_keys("1Qazxsw2@")

   time.sleep(1)
   login_button = driver.find_element(By.XPATH, "//button[@type = 'submit']")
   login_button.click()

   ignore_list = [NoSuchElementException, ElementNotSelectableException,StaleElementReferenceException]
   wait = WebDriverWait(driver,20, poll_frequency=1, ignored_exceptions=ignore_list)
   element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']")))
   link = driver.current_url
   print("The current url is:" + str(link))
   if link == "https://dev.eminusgroup.com/#/app/adminHomeDashboard":
       print(" A status is: LOGIN SUCCESSFUL")
   else:
       error_nottification = driver.find_element(By.XPATH, "//div[@class='row justify-center q-pt-sm q-pb-md']")
       print(error_nottification.text)

def em_solution_links():
   buttons=driver.find_elements(By.XPATH,"//button[@type='button']")
   print(buttons[1].text)
   for solutionlink in buttons:
       if solutionlink.text=="link\nResource Links":
           solutionlink.click()


   time.sleep(5)
   form=driver.find_element(By.XPATH,"//div[@class='q-pa-md link']")
   driver.implicitly_wait(2)
   ActionChains(driver).move_to_element(form).click(form).perform()

   time.sleep(4)
   options=driver.find_elements(By.XPATH,"//button[@type='button']")
   for edit_btn in options:
       if edit_btn.text=="edit\nEdit links":
           driver.execute_script("arguments[0].click()",edit_btn)

   link_btn=driver.find_elements(By.XPATH,"//button[@type='button']")
   print("Type of link_btn:",type(link_btn))
   button_list=[]
   for add_link in link_btn:
       print(add_link.text)
       if add_link.text=="add\nAdd link":
           button_list.append(add_link)
   len_addlink_btns=len(button_list)
   print("Length of button list",len_addlink_btns)
   if len_addlink_btns>0:
       button_list[0].click()
       text_insidexbox=driver.find_elements(By.XPATH,"//input[@type='text']")
       for empty_box in text_insidexbox:
           empty_boxes=empty_box.get_attribute("value")
           if empty_boxes=="":


   time.sleep(2)
   link_boxes=
   print("Length of link boxes:",link_boxes_count)
   if link_boxes_count>0:

       link_boxes[0].send_keys(Keys.CONTROL+"a")
       link_boxes[0].send_keys(Keys.DELETE)
       link_boxes[0].send_keys("linktext.co")


   save_option=driver.find_elements(By.XPATH,"//button[@type='button']")
   for save_button in save_option:
       if save_button.text=="Save Changes":
           save_button.click()

   driver.implicitly_wait(5)
   card=driver.find_element(By.XPATH,"//div[@class='q-card__section q-card__section--vert row justify-center text-subtitle2 text-weight-bold q-pt-none']")
   print("Nottification:",card.text)
   print("__________________")


em_login()
em_solution_links()
