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

    time.sleep(10)
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        msg = driver.find_element(By.XPATH,"//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(msg)
        if "Please verify your email" in msg:
            print(" A status is: LOGIN NOT SUCCESS")

    #button in the particular card is type = 'submit' it have only one btn
    #button in the top of the page is type= 'button'
    #in type='button', [o] is homedashboard and [1] is next in top

def emaddclient():

    time.sleep(4)
    addclient=driver.find_elements(By.TAG_NAME,"i")
    print("i tag length:",len(addclient))
    addclient[4].click()  #4th i tag for the add client btn



def emaddclientprofile():  #create the client with already existing company name in that CPA

    time.sleep(4)
    companyname = driver.find_elements(By.XPATH,"//input[@class='q-field__native q-placeholder']")
    print("lenth of textbox:",len(companyname))
    companyname[0].send_keys("autouser8a") #existing company name

    industry = driver.find_elements(By.XPATH,"//input[@role='combobox']")
    print("length of combobox:",len(industry))
    industryselect=industry[0]
    ActionChains(driver).move_to_element(industryselect).click(industryselect).perform()
    time.sleep(2)
    industryvalue=driver.find_elements(By.CLASS_NAME,"q-item__label")
    print("length of industries:",len(industryvalue))
    industryvalue[4].click()

    state = driver.find_elements(By.XPATH, "//input[@role='combobox']")
    print("lengh of combobox:",len(state))
    stateselect = state[1]
    ActionChains(driver).move_to_element(stateselect).click(stateselect).perform()
    time.sleep(2)
    statevalue = driver.find_elements(By.CLASS_NAME, "q-item__label")
    print("length of states:",len(statevalue))
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
    submitbtn = driver.find_elements(By.XPATH,"//button[@type='submit']")
    print("length of submit button",len(submitbtn))
    submitbtn[0].click()


def emyearquarter():

    combobox = driver.find_elements(By.XPATH,"//input[@role='combobox']")
    print("length of comboboxes in add data screen:",len(combobox))

    #selecting a year
    years=combobox[0]
    ActionChains(driver).move_to_element(years).click(years).perform()
    time.sleep(1)
    yearvalue = driver.find_elements(By.CLASS_NAME, "q-item__label")
    print("length of years:", len(yearvalue))
    yearvalue[4].click()

    #selecting the quarter
    quarter = combobox[1]
    ActionChains(driver).move_to_element(quarter).click(quarter).perform()
    time.sleep(1)
    quartervalue = driver.find_elements(By.CLASS_NAME, "q-item__label")
    print("length of qaurter:", len(quartervalue))
    quartervalue[3].click()

def emdataadd():

    time.sleep(1)
    revenue = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    revenueselect = revenue[0]
    print("length of fields:", len(revenue))
    ActionChains(driver).move_to_element(revenueselect).click(revenueselect).perform()
    revenuevalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    print("No of data entry fields",len(revenuevalue))
    revenuevalue[0].send_keys("44300")

    time.sleep(1)
    currentassest = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    currentassestselect = currentassest[1]
    ActionChains(driver).move_to_element(currentassestselect).click(currentassestselect).perform()
    assetvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(assetvalue))
    assetvalue[1].send_keys("223201")

    time.sleep(1)
    currentliliability = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    currentlilselect = currentliliability[2]
    ActionChains(driver).move_to_element(currentlilselect).click(currentlilselect).perform()
    currentlilvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(currentlilvalue))
    currentlilvalue[2].send_keys("85802")

    time.sleep(1)
    quota = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    quotaselect = quota[3]
    ActionChains(driver).move_to_element(quotaselect).click(quotaselect).perform()
    quotavalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(quotavalue))
    quotavalue[3].send_keys("85803")

    time.sleep(1)
    pipelinecost = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    pipelinecostselect = pipelinecost[4]
    ActionChains(driver).move_to_element(pipelinecostselect).click(pipelinecostselect).perform()
    pipelinecostvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(pipelinecostvalue))
    pipelinecostvalue[4].send_keys("85804")

    time.sleep(1)
    grossprofit = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    grossprofitselect = grossprofit[5]
    ActionChains(driver).move_to_element(grossprofitselect).click(grossprofitselect).perform()
    grossprofitvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(grossprofitvalue))
    grossprofitvalue[5].send_keys("85805")

    time.sleep(1)
    rdcost = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    rdcostselect = rdcost[6]
    ActionChains(driver).move_to_element(rdcostselect).click(rdcostselect).perform()
    rdcostvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(rdcostvalue))
    rdcostvalue[6].send_keys("85806")

    time.sleep(1)
    smcost = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    smcostselect = smcost[7]
    ActionChains(driver).move_to_element(smcostselect).click(smcostselect).perform()
    smcostvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(smcostvalue))
    smcostvalue[7].send_keys("85807")

    time.sleep(1)
    gacost = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    gacostselect = gacost[8]
    ActionChains(driver).move_to_element(gacostselect).click(gacostselect).perform()
    gacostvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(gacostvalue))
    gacostvalue[8].send_keys("85808")

    time.sleep(1)
    ebitda = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    ebitdaselect = ebitda[9]
    ActionChains(driver).move_to_element(ebitdaselect).click(ebitdaselect).perform()
    ebitdavalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(ebitdavalue))
    ebitdavalue[9].send_keys("85809")

    time.sleep(1)
    cashbalance = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    cashbalanceselect = rdcost[10]
    ActionChains(driver).move_to_element(cashbalanceselect).click(cashbalanceselect).perform()
    cashbalancevalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(cashbalancevalue))
    cashbalancevalue[10].send_keys("858010")

    time.sleep(1)
    burnrate = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    burnrateselect = burnrate[11]
    ActionChains(driver).move_to_element(burnrateselect).click(burnrateselect).perform()
    burnratevalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(burnratevalue))
    burnratevalue[11].send_keys("858011")

    time.sleep(1)
    emboy = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    emboyselect = emboy[12]
    ActionChains(driver).move_to_element(emboyselect).click(emboyselect).perform()
    emboyvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(emboyvalue))
    emboyvalue[12].send_keys("85812")

    time.sleep(1)
    emeoy = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    emeoyselect = emeoy[13]
    ActionChains(driver).move_to_element(emeoyselect).click(emeoyselect).perform()
    emeoyvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(emeoyvalue))
    emeoyvalue[13].send_keys("858013")

    time.sleep(1)
    customerchurn = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    customerchurnselect = customerchurn[14]
    ActionChains(driver).move_to_element(customerchurnselect).click(customerchurnselect).perform()
    customerchurnvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(customerchurnvalue))
    customerchurnvalue[14].send_keys("858014")

    time.sleep(1)
    fixedcost = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    fixedcostselect = fixedcost[15]
    ActionChains(driver).move_to_element(fixedcostselect).click(fixedcostselect).perform()
    fixedcostvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(fixedcostvalue))
    fixedcostvalue[15].send_keys("858015")

    time.sleep(1)
    ltv = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    ltvselect = ltv[16]
    ActionChains(driver).move_to_element(ltvselect).click(ltvselect).perform()
    ltvvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(ltvvalue))
    ltvvalue[16].send_keys("858016")

    time.sleep(1)
    customeracqcost = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    customeracqcostselect = customeracqcost[17]
    ActionChains(driver).move_to_element(customeracqcostselect).click(customeracqcostselect).perform()
    customeracqcostvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(customeracqcostvalue))
    customeracqcostvalue[17].send_keys("858017")

    time.sleep(1)
    boyboq = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    boyboqselect = boyboq[18]
    ActionChains(driver).move_to_element(boyboqselect).click(boyboqselect).perform()
    boyboqvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(boyboqvalue))
    boyboqvalue[18].send_keys("858018")

    time.sleep(1)
    eoyeoq = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    eoyeoqselect = eoyeoq[19]
    ActionChains(driver).move_to_element(eoyeoqselect).click(eoyeoqselect).perform()
    eoyeoqvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(eoyeoqvalue))
    eoyeoqvalue[19].send_keys("858019")

    time.sleep(1)
    eechurn = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    eechurnselect = eechurn[20]
    ActionChains(driver).move_to_element(eechurnselect).click(eechurnselect).perform()
    eechurnvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(eechurnvalue))
    eechurnvalue[20].send_keys("858020")

    time.sleep(1)
    opcashflow = driver.find_elements(By.XPATH, "//div[@class='metric-width']")
    opcashflowselect = opcashflow[21]
    ActionChains(driver).move_to_element(opcashflowselect).click(opcashflowselect).perform()
    opcashflowvalue = driver.find_elements(By.XPATH, "//input[@type='number']")
    #print(len(opcashflowvalue))
    opcashflowvalue[21].send_keys("858021")

    #submit
    submitbtn = driver.find_elements(By.XPATH,"//button[@type='button']")
    print(len(submitbtn))
    for btn in submitbtn:
        print(btn.get_attribute('innerHTML'))

    submitbtn[2].click()

    time.sleep(5)
    statement = driver.current_url
    print("current url:",statement)
    if statement =="https://dev.eminusgroup.com/#/app/homeDashboard":
        print("Client created")
    else:
        time.sleep(2)
        card = driver.find_element(By.XPATH, "//div[@class='q-card']")
        print(card.text)



        okbtn = driver.find_elements(By.XPATH, "//button[@type='button']")
        print(len(okbtn))
        print(okbtn[4].text)
        okbtn[4].click()



emlogin()
emaddclient()
emaddclientprofile()
emyearquarter()
emdataadd()