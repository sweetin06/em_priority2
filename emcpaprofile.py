import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://dev.eminusgroup.com/#/")


def em_login():

    time.sleep(2)
    username = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Email']")
    username.send_keys("patric@devaxcel.com")

    time.sleep(1)
    password = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Password']")
    password.send_keys("1Qazxsw2@")

    time.sleep(1)
    signin_button = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    signin_button.click()

    ignore_list = [NoSuchElementException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    element = wait.until(EC.element_to_be_clickable((By.ID, "appHeader_profile_btn")))
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        msg = driver.find_element(By.XPATH, "//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(msg)
        if "Please verify your email" in msg:
            print(" A status is: LOGIN NOT SUCCESS")

def em_cpa_profile():

    time.sleep(2)
    profilebar = driver.find_element(By.ID, "appHeader_profile_btn")
    profilebar.click()
    time.sleep(1)
    my_profile_option = driver.find_element(By.ID,"profile_btn_myProfile")
    my_profile_option.click()

    time.sleep(2)
    form = driver.find_elements(By.XPATH,"//form[@class='q-form']")
    print("qforms:", len(form))
    ActionChains(driver).move_to_element(form[0]).click(form[0]).perform()

    time.sleep(2)
    editbtns = driver.find_elements(By.XPATH, "//button[@type='submit']")
    driver.implicitly_wait(2)
    print("No of buttons:", len(editbtns))
    for edit_btn in editbtns:
        if edit_btn.text=="Edit Information":
            driver.execute_script("arguments[0].click()",edit_btn)

def em_edit_cpa():

    time.sleep(1)
    textboxes=driver.find_elements(By.XPATH,"//input[@type='text']")
    print("No of textboxes:",len(textboxes))

    time.sleep(1)
    comboboxes = driver.find_elements(By.XPATH,"//input[@role='combobox']")
    print("No of comboboxes:",len(comboboxes))

    time.sleep(1)
    first_name=textboxes[0]
    first_name.send_keys(Keys.CONTROL+"a")
    first_name.send_keys(Keys.DELETE)
    first_name.send_keys("automation")

    time.sleep(1)
    last_name = textboxes[1]
    last_name.send_keys(Keys.CONTROL + "a")
    last_name.send_keys(Keys.DELETE)
    last_name.send_keys("client")

    """time.sleep(1) This is for email.it not editable
    firstname = driver.find_elements(By.XPATH, "//input[@type='text']")[2]
    firstname.send_keys(Keys.CONTROL + "a")
    firstname.send_keys(Keys.DELETE)
    firstname.send_keys("autoclient@devaxcel.com")"""

    time.sleep(1)
    phone_no = textboxes[3]
    phone_no.send_keys(Keys.CONTROL + "a")
    phone_no.send_keys(Keys.DELETE)
    phone_no.send_keys("8888888880")

    time.sleep(1)
    time.sleep(1)
    firm_name = textboxes[4]
    firm_name.send_keys(Keys.CONTROL + "a")
    firm_name.send_keys(Keys.DELETE)
    firm_name.send_keys("autocomp")

    time.sleep(1)
    address = textboxes[5]
    address.send_keys(Keys.CONTROL + "a")
    address.send_keys(Keys.DELETE)
    address.send_keys("addauto")


    time.sleep(1)
    partners=comboboxes[0]
    driver.implicitly_wait(2)
    driver.execute_script("arguments[0].click()",partners)
    time.sleep(2)
    partner_select = driver.find_elements(By.CLASS_NAME,"q-item__label")
    for partner in partner_select:
        if partner.text=="2-5":
            partner.click()
            break

    time.sleep(1)
    clients = comboboxes[1]
    driver.implicitly_wait(2)
    driver.execute_script("arguments[0].click()",clients)
    time.sleep(2)
    client_select = driver.find_elements(By.CLASS_NAME,"q-item__label")
    for client in client_select:
        if client.text=="2-5":
            client.click()
            break

    time.sleep(2)
    offices = comboboxes[2]
    driver.implicitly_wait(2)
    driver.execute_script("arguments[0].click()", offices)
    office_select = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    time.sleep(2)
    for office in office_select:
        if office.text=="2-5":
            office.click()
            break


    time.sleep(1)
    states = comboboxes[3]
    driver.implicitly_wait(2)
    driver.execute_script("arguments[0].click()",states)
    state_select = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    time.sleep(2)
    for state in state_select:
        if state.text=="Lowa":
            state.click()
            break

    time.sleep(2)
    profile=driver.find_element(By.ID,"filePick")
    profile.send_keys("//home//applings//Downloads//cpaauto.jpg")

    submit_btn=driver.find_element(By.XPATH,"//button[@type='submit']")
    driver.execute_script("arguments[0].click()",submit_btn)

    time.sleep(3)
    message_notification = driver.find_element(By.XPATH, "//div[@class='q-notification__message col']")
    print(message_notification.text)


em_login()
em_cpa_profile()
em_edit_cpa()
