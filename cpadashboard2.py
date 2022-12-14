import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


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


def cpadashboardfilters():

    #values to be selected
    name = "client"
    revenuefield="$5.0M to $6.0M"
    industryfield="Software"
    statefield="Alabama"
    statusfield="Active Clients"


    time.sleep(2)
    search=driver.find_element(By.XPATH,"//input[@type='text']")
    search.send_keys(name)

    comboboxes=driver.find_elements(By.XPATH,"//input[@role='combobox']")
    print("length of comboboxes:",len(comboboxes))
    """for com in comboboxes:
        print(com.get_attribute("innerHTML"))"""


    time.sleep(2)
    revenue=comboboxes[0]
    driver.execute_script("arguments[0].click()",revenue)
    time.sleep(1)
    revenuelists=driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
    for revenuelist in revenuelists:
        if revenuelist.text==revenuefield:
            revenuelist.click()

    time.sleep(2)
    industry=comboboxes[1]
    driver.execute_script("arguments[0].click()",industry)
    time.sleep(1)
    industrylists=driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
    for industrylist in industrylists:
        if industrylist.text==industryfield:
            industrylist.click()
        """elif industrylist.text=="Finance":
            industrylist.click()"""
    ActionChains(driver).move_to_element(industry).click(industry).perform()

    time.sleep(1)
    states=comboboxes[2]
    driver.execute_script("arguments[0].click()",states)
    time.sleep(5)
    statelists=driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
    for statelist in statelists:
        if statelist.text==statefield:
            statelist.click()
        """elif statelist.text=="Delaware":
            statelist.click()"""
    ActionChains(driver).move_to_element(states).click(states).perform()
    time.sleep(2)

    status=comboboxes[3]
    driver.execute_script("arguments[0]",status)
    time.sleep(1)
    statuslists=driver.find_elements(By.XPATH,"//div[@class='q-item__label']")
    for statuslist in statuslists:
        if statuslist.text==statusfield:
            statuslist.click()


    try:
        time.sleep(2)
        errmsg = driver.find_element(By.XPATH, "//div[@class='row justify-center q-pt-md']")
        print("okk")

    except NoSuchElementException:
        print("A Deatils Selected")
        time.sleep(2)
        table = driver.find_element(By.XPATH, "//table[@class='q-table']")
        driver.implicitly_wait(2)
        ActionChains(driver).move_to_element(table).click(table).perform()
        time.sleep(5)
        rowcount = driver.find_elements(By.XPATH, "//tbody[@class='q-virtual-scroll__content']//tr")
        print("rowcounts:", len(rowcount))
        rowcounts = len(rowcount)
        time.sleep(1)
        colcount = driver.find_elements(By.XPATH, "//table[@class='q-table']//th")
        print("Columnscount:", len(colcount))
        colcounts = len(colcount)
        for row in range(1, rowcounts + 1):
            # for col in range(1,colcounts):
            time.sleep(2)
            values = driver.find_element(By.XPATH, "//table[@class='q-table']")
            ActionChains(driver).move_to_element(values).click(values).perform()
            time.sleep(4)
            # below is the crt line
            contents = driver.find_element(By.XPATH,"//tbody[@class='q-virtual-scroll__content']//tr[" + str(row) + "]")
            rowContent = contents.text
            #print('the row content is ', rowContent) #print the table content
            #print(type(rowContent))
            if (name and revenuefield) and (industryfield and statefield) in rowContent:
                print("Details matched with filtered item")
            else:
                print("Details mis-matched with filtered item")

    else:
        print("Details unmatched")
        print(errmsg.text)

    finally:
        print("__________________________")


emlogin()
cpadashboardfilters()