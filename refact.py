import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from office import emlogin


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#get the url
driver.get("https://dev.eminusgroup.com/#/")

def emcpaprofile():


    time.sleep(2)
    profilebar = driver.find_element(By.ID, "appHeader_profile_btn")
    profilebar.click()
    time.sleep(1)
    myprofileoption = driver.find_element(By.ID,"profile_btn_myProfile")
    myprofileoption.click()

def emcpaeditbtn():

    #tab=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By. XPATH,"//form[@class='q-form']")))
    time.sleep(2)
    tab = driver.find_elements(By.XPATH,"//form[@class='q-form']")
    print("qforms:", len(tab))
    ActionChains(driver).move_to_element(tab[0]).click(tab[0]).perform()


    time.sleep(2)
    editbtns = driver.find_elements(By.XPATH, "//button[@type='submit']")
    driver.implicitly_wait(2)
    print("btns:", len(editbtns))
    print(editbtns[0].text)
    editbtn = editbtns[0]
    driver.execute_script("arguments[0].click()", editbtn)

def emeditcpa():

    time.sleep(1)
    textboxes=driver.find_elements(By.XPATH,"//input[@type='text']")
    print("No of textboxes:",len(textboxes))

    time.sleep(1)
    firstname=driver.find_elements(By.XPATH,"//input[@type='text']")[0]
    firstname.send_keys(Keys.CONTROL+"a")
    firstname.send_keys(Keys.DELETE)
    firstname.send_keys("automation")

    time.sleep(1)
    lastname = driver.find_elements(By.XPATH, "//input[@type='text']")[1]
    lastname.send_keys(Keys.CONTROL + "a")
    lastname.send_keys(Keys.DELETE)
    lastname.send_keys("client")

    # a email field s not editable
    """time.sleep(1) This is for email.it not editable
    firstname = driver.find_elements(By.XPATH, "//input[@type='text']")[2]
    firstname.send_keys(Keys.CONTROL + "a")
    firstname.send_keys(Keys.DELETE)
    firstname.send_keys("autoclient@devaxcel.com")"""

    time.sleep(1)
    lastname = driver.find_elements(By.XPATH, "//input[@type='text']")[3]
    lastname.send_keys(Keys.CONTROL + "a")
    lastname.send_keys(Keys.DELETE)
    lastname.send_keys("8888888880")

    time.sleep(1)
    time.sleep(1)
    firmname = driver.find_elements(By.XPATH, "//input[@type='text']")[4]
    firmname.send_keys(Keys.CONTROL + "a")
    firmname.send_keys(Keys.DELETE)
    firmname.send_keys("autocomp")

    time.sleep(1)
    lastname = driver.find_elements(By.XPATH, "//input[@type='text']")[5]
    lastname.send_keys(Keys.CONTROL + "a")
    lastname.send_keys(Keys.DELETE)
    lastname.send_keys("addauto")

    comboboxes=driver.find_elements(By.XPATH,"//input[@role='combobox']")
    print("No of comboboxes",len(comboboxes))
    print(comboboxes[2].text)
    for combo in comboboxes:
        print(combo.get_attribute("innerHTML"))

    time.sleep(1)
    partners = driver.find_elements(By.XPATH,"//input[@role='combobox']")[0]
    driver.implicitly_wait(2)
    driver.execute_script("arguments[0].click()",partners)
    time.sleep(2)
    partnerselect = driver.find_elements(By.CLASS_NAME,"q-item__label")
    print("list of partners", len(partnerselect))
    time.sleep(2)
    partnerselect[4].click()

    time.sleep(1)
    clients = driver.find_elements(By.XPATH, "//input[@role='combobox']")[1]
    driver.implicitly_wait(2)
    driver.execute_script("arguments[0].click()",clients)
    time.sleep(2)
    clientselect = driver.find_elements(By.CLASS_NAME,"q-item__label")
    print("list of clients", len(clientselect))
    time.sleep(2)
    clientselect[3].click()

    time.sleep(2)
    offices = driver.find_elements(By.XPATH, "//input[@role='combobox']")[2]
    driver.implicitly_wait(2)
    driver.execute_script("arguments[0].click()", offices)
    # ActionChains(driver).move_to_element(offices).click(offices).perform()
    officeselect = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    time.sleep(2)
    print("list of offices", len(officeselect))
    officeselect[2].click()


    time.sleep(1)
    states = driver.find_elements(By.XPATH,"//input[@role='combobox']")[3]
    driver.implicitly_wait(2)
    driver.execute_script("arguments[0].click()",states)
    time.sleep(2)
    state = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    print("state", len(state))
    time.sleep(2)
    state[28].click()


def empro():
    time.sleep(2)
    pic=driver.find_element(By.ID,"filePick")
    pic.send_keys("//home//applings//Downloads//cpaauto.jpg")

    submitbtn=driver.find_element(By.XPATH,"//button[@type='submit']")
    driver.execute_script("arguments[0].click()",submitbtn)

    time.sleep(3)
    msg = driver.find_element(By.XPATH, "//div[@class='q-notification__message col']")
    print(msg.text)

    """ActionChains(driver).move_to_element(pic[0]).click(pic[0]).perform()
    pic.send_keys("home\\applings\\Downloads\\cpaauto.jpg")"""

emlogin()
emcpaprofile()
emcpaeditbtn()
emeditcpa()
empro()