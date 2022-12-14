import time
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver import ActionChains
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
#get the url
driver.get("https://dev.eminusgroup.com/#/")

def em_login():
    time.sleep(2)
    UserName = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Email']")
    UserName.send_keys("patric@devaxcel.com")

    time.sleep(1)
    Password = driver.find_element(By.XPATH,"//input[@aria-label='Enter Your Password']")
    Password.send_keys("1Qazxsw2@")

    time.sleep(1)
    Button = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    Button.click()

    """wait.WebDriverWait(driver,10,2,ignored_exceptions=[NoSuchElementException])
    wait.WebDriverWait.until(EC.element_to_be_clickable(By.ID, "appHeader_profile_btn"))"""
    ignore_list = [NoSuchElementException, ElementNotSelectableException]
    wait = WebDriverWait(driver,10, poll_frequency=1, ignored_exceptions=NoSuchElementException)
    element = wait.until(EC.element_to_be_clickable((By.ID, "appHeader_profile_btn")))
    #wait.until(EC.element_to_be_clickable(By.ID, "appHeader_profile_btn"))
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        Msg = driver.find_element(By.XPATH,"//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(Msg)
        if "Please verify your email" in Msg:
            print(" A status is: LOGIN NOT SUCCESS")

def em_metric():

    time.sleep(10)
    tags = driver.find_elements(By.XPATH, "//button[@dropdownicon='more_vert']")
    print("tags:", len(tags))
    """for tag in tags:
        print(tag.get_attribute("innerHTML"))
"""

    PreviousYearRevenue=12000000
    CurrentYearRevenue=15000000
    CurrentAssests=1562000
    CurrentLiliability=1200000
    Quota=4000000
    PipelineCost=5200000
    GrossProfit=13000000
    RDCost=3500000
    SMCost=2800000
    GACost=1900000
    Ebitda=1100000
    CashBalance=1200000
    BurnRate=40000
    Employee_BOY=212
    Employee_EOY=248
    CustomerChurn=235000
    FixedCosts=8000000
    LifeTimeValue=25000
    CustomerAcquisitionCost=4000
    ARBoyandBoq=895000
    AREoyandEoq=1100000
    EEChurn=22
    OPCashflow=125000


    cagr_calc= ((CurrentYearRevenue-PreviousYearRevenue)/PreviousYearRevenue)*100

    PiplinecovCalc=PipelineCost/Quota
    GPperCalc=GrossProfit/CurrentYearRevenue
    RDCalc=RDCost/CurrentYearRevenue
    SMCalc=SMCost/CurrentYearRevenue
    GACalc=GACost/CurrentYearRevenue
    EbitdaPerCalc=Ebitda/CurrentYearRevenue
    CashRunWayCalc=CashBalance/BurnRate
    RevandEECalc=CurrentYearRevenue/((Employee_BOY/Employee_EOY)/2)
    CustChurnCalc=CustomerChurn/CurrentYearRevenue
    BreakEvenCalc=FixedCosts/GPperCalc
    LTCCACCalc=LifeTimeValue/CustomerAcquisitionCost
    CurrentRatioCalc=CurrentAssests/CurrentLiliability
    EEChurnCalc=EEChurn
    OPCashflowcalc=OPCashflow
    ArDSOCalc=CurrentYearRevenue//((ARBoyandBoq+AREoyandEoq)/2)
    Ruleof40Calc=cagr_calc+Ebitda


    time.sleep(2)
    tag0 = tags[0]
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(tag0).click(tag0).perform()
    metricoption = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    print("options", len(metricoption))
    metricoption[0].click()
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=StaleElementReferenceException)
    table = wait.until(EC.element_to_be_clickable((By.XPATH,"//table[@class='q-table']")))
    #table=driver.find_elements(By.XPATH,"//table[@class='q-table']")

    driver.execute_script("arguments[0].click()",table)
    time.sleep(2)
    cagr=driver.find_element(By.XPATH,"//table/tbody/tr[1]/td[2]")
    cagr_value=cagr.text
    print("value from table:",cagr_value)
    cagr_calc = round(cagr_calc)
    cagr_calc = (f"{cagr_calc}%")
    print("value from calc",cagr_value)
    print(cagr_calc)
    if cagr_calc==cagr_value:
        print("ok")
    else:
        print("A value get differ")


em_login()
em_metric()