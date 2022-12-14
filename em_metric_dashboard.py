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
# get the url
driver.get("https://dev.eminusgroup.com/#/")


def em_login():
    time.sleep(2)
    username = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Email']")
    username.send_keys("calculation@devaxcel.com")

    time.sleep(1)
    password = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Password']")
    password.send_keys("1Qazxsw2@")

    time.sleep(1)
    signinbutton = driver.find_element(By.XPATH, "//button[@type = 'submit']")
    signinbutton.click()

    ignore_list = [NoSuchElementException, ElementNotSelectableException]
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=ignore_list)
    element = wait.until(EC.element_to_be_clickable((By.ID, "appHeader_profile_btn")))
    # wait.until(EC.element_to_be_clickable(By.ID, "appHeader_profile_btn"))
    link = driver.current_url
    print("The current url is:" + str(link))
    if link == "https://dev.eminusgroup.com/#/app/homeDashboard":
        print(" A status is: LOGIN SUCCESSFUL")
    else:
        error_nottification = driver.find_element(By.XPATH, "//div[@class='row justify-center q-pt-sm q-pb-md']").text
        print(error_nottification)
        if "Please verify your email" in error_nottification:
            print(" A status is: LOGIN NOT SUCCESS")


def em_metric():
    driver.implicitly_wait(2)
    elipses = driver.find_elements(By.XPATH, "//button[@dropdownicon='more_vert']")
    print("Total elipses in table:", len(elipses))
    time.sleep(2)
    elipses0 = elipses[0]
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(elipses0).click(elipses0).perform()
    metric_option = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
    print("options", len(metric_option))
    metric_option[0].click()

    # values assigned for client1
    previous_year_revenue_c1 = 12000000
    current_year_revenue_c1 = 15000000
    current_assests_c1 = 1562000
    current_liliability_c1 = 1200000
    quota_c1 = 4000000
    pipeline_cost_c1 = 5200000
    gross_profit_c1 = 13000000
    rd_cost_c1 = 3500000
    sm_cost_c1 = 2800000
    ga_cost_c1 = 1900000
    ebitda_c1 = 1100000
    cash_balance_c1 = 1200000
    burn_rate_c1 = 40000
    employee_boy_c1 = 212
    employee_eoy_c1 = 248
    customer_churn_c1 = 235000
    fixed_costs_c1 = 8000000
    life_time_value_c1 = 25000
    customer_acquisition_cost_c1 = 4000
    ar_boy_and_boq_c1 = 895000
    ar_eoy_and_eoq_c1 = 1100000
    ee_churn_c1 = 22
    op_cash_flow_c1 = 125000

    # calculation  of client1
    cagr_calc_c1 = ((current_year_revenue_c1 - previous_year_revenue_c1) / previous_year_revenue_c1) * 100
    pipeline_cov_calc_c1 = (pipeline_cost_c1 / quota_c1)
    gp_per_calc_c1 = (gross_profit_c1 / current_year_revenue_c1) * 100
    rd_calc_c1 = (rd_cost_c1 / current_year_revenue_c1) * 100
    sm_calc_c1 = (sm_cost_c1 / current_year_revenue_c1) * 100
    ga_calc_c1 = (ga_cost_c1 / current_year_revenue_c1) * 100
    ebitda_calc_c1 = (ebitda_c1 / current_year_revenue_c1) * 100
    cash_runway_calc_c1 = (cash_balance_c1 / burn_rate_c1)
    rev_and_ee_calc_c1 = current_year_revenue_c1 / ((employee_boy_c1 + employee_eoy_c1) / 2)
    cust_churn_calc_c1 = (customer_churn_c1 / current_year_revenue_c1) * 100
    break_even_calc_c1 = (fixed_costs_c1 / gp_per_calc_c1) * 100
    ltc_cac_calc_c1 = (life_time_value_c1 / customer_acquisition_cost_c1)
    current_ratio_calc_c1 = (current_assests_c1 / current_liliability_c1)
    ee_churn_calc_c1 = ee_churn_c1
    op_cashflow_calc_c1 = op_cash_flow_c1
    ar_dso_calc_c1 = (current_year_revenue_c1 // ((ar_boy_and_boq_c1 + ar_eoy_and_eoq_c1) / 2))
    rule_of40_calc_c1 = cagr_calc_c1 + ebitda_calc_c1

    # values assigned  for client 2
    previous_year_revenue_c2 = 11000000
    current_year_revenue_c2 = 13000000
    current_assests_c2 = 1562000
    current_liliability_c2 = 900000
    quota_c2 = 4000000
    pipeline_cost_c2 = 5200000
    gross_profit_c2 = 13000000
    rd_cost_c2 = 3500000
    sm_cost_c2 = 2000000
    ga_cost_c2 = 1900000
    ebitda_c2 = 1100000
    cash_balance_c2 = 1400000
    burn_rate_c2 = 40000
    employee_boy_c2 = 212
    employee_eoy_c2 = 248
    customer_churn_c2 = 235000
    fixed_costs_c2 = 8000000
    life_time_value_c2 = 25000
    customer_acquisition_cost_c2 = 4000
    ar_boy_and_boq_c2 = 895000
    ar_eoy_and_eoq_c2 = 1100000
    ee_churn_c2 = 32
    op_cash_flow_c2 = 105000

    # calculation of client2
    cagr_calc_c2 = ((current_year_revenue_c2 - previous_year_revenue_c2) / previous_year_revenue_c2) * 100
    pipeline_cov_calc_c2 = (pipeline_cost_c2 / quota_c2)
    gp_per_calc_c2 = (gross_profit_c2 / current_year_revenue_c2) * 100
    rd_calc_c2 = (rd_cost_c2 / current_year_revenue_c2) * 100
    sm_calc_c2 = (sm_cost_c2 / current_year_revenue_c2) * 100
    ga_calc_c2 = (ga_cost_c2 / current_year_revenue_c2) * 100
    ebitda_calc_c2 = (ebitda_c2 / current_year_revenue_c2) * 100
    cash_runway_calc_c2 = (cash_balance_c2 / burn_rate_c2)
    rev_and_ee_calc_c2 = current_year_revenue_c2 / ((employee_boy_c2 + employee_eoy_c2) / 2)
    cust_churn_calc_c2 = (customer_churn_c2 / current_year_revenue_c2) * 100
    break_even_calc_c2 = (fixed_costs_c2 / gp_per_calc_c2) * 100
    ltc_cac_calc_c2 = (life_time_value_c2 / customer_acquisition_cost_c2)
    current_ratio_calc_c2 = (current_assests_c2 / current_liliability_c2)
    ee_churn_calc_c2 = ee_churn_c2
    op_cashflow_calc_c2 = op_cash_flow_c2
    ar_dso_calc_c2 = (current_year_revenue_c2 // ((ar_boy_and_boq_c2 + ar_eoy_and_eoq_c2) / 2))
    rule_of40_calc_c2 = cagr_calc_c1 + ebitda_calc_c2

    # business segment calculation
    business_segment_cagr = (cagr_calc_c1 + cagr_calc_c2) / 2
    business_segment_pipeline = (pipeline_cov_calc_c1 + pipeline_cov_calc_c2) / 2
    business_segment_gpper = (gp_per_calc_c1 + gp_per_calc_c2) / 2
    business_segment_rd = (rd_calc_c1 + rd_calc_c2) / 2
    business_segment_sm = (sm_calc_c1 + sm_calc_c2) / 2
    business_segment_ga = (ga_calc_c1 + ga_calc_c2) / 2
    business_segment_ebitda = (ebitda_calc_c1 + ebitda_calc_c2) / 2
    business_segment_cashrunway = (cash_runway_calc_c1 + cash_runway_calc_c2) / 2
    business_segment_rev_ee = (rev_and_ee_calc_c1 + rev_and_ee_calc_c2) / 2
    business_segment_custchurn = (cust_churn_calc_c1 + cust_churn_calc_c2) / 2
    business_segment_breakeven = (break_even_calc_c1 + break_even_calc_c2) / 2
    business_segment_ltv_cac = (ltc_cac_calc_c1 + ltc_cac_calc_c2) / 2
    business_segment_current_ratio = (current_ratio_calc_c1 + current_ratio_calc_c2) / 2
    business_segment_eechurn = (ee_churn_calc_c1 + ee_churn_calc_c2) / 2
    business_segment_opcashflow = (op_cashflow_calc_c1 + op_cashflow_calc_c2) / 2
    business_segment_ardso = (ar_dso_calc_c1 + ar_dso_calc_c2) / 2
    business_segment_rule40 = (rule_of40_calc_c1 + rule_of40_calc_c2) / 2

    # RATIO CALCULATION CLIENT1
    ignore_list = [NoSuchElementException, ElementNotSelectableException,StaleElementReferenceException]
    wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=ignore_list)
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"//table[@class='q-table']")))
    print("----RATIO CALCULATION---- FIRST CLIENT")
    table=driver.find_element(By.XPATH,"//table[@class='q-table']")
    driver.implicitly_wait(2)
    ActionChains(driver).move_to_element(table).perform()

    # cagr_calculation
    time.sleep(1)
    cagr_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[2]").text
    cagr_modify_c1 = float(cagr_value_c1.strip("%"))
    round_cagr_c1=round(cagr_modify_c1)
    cagr_table_c1=(f"{round_cagr_c1}%")
    print("CAGR value from table=",cagr_table_c1)
    round_cagr_calc_c1 = round(cagr_calc_c1)
    cagr_result_calc_c1 = (f"{round_cagr_calc_c1}%")
    print("CAGR value from calc=", cagr_result_calc_c1)
    if cagr_result_calc_c1 == cagr_table_c1:
        print("CAGR CALCULATION IS MATCHED")
    else:
        print("CAGR CALCULATION IS MIS-MATCHED")

    # pipelinecov_calculation
    time.sleep(1)
    pipeline_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[2]").text
    pipeline_modify_c1 = float(pipeline_value_c1.strip("%"))
    round_pipeline_c1 = round(pipeline_modify_c1)
    pipeline_table_c1 = (f"{round_pipeline_c1}%")
    print("pipeline value from table=", pipeline_table_c1)
    round_pipeline_calc_c1 = round(pipeline_cov_calc_c1)
    pipeline_result_calc_c1 = (f"{round_pipeline_calc_c1}%")
    print("pipeline value from calc=", pipeline_result_calc_c1)
    if pipeline_result_calc_c1 == pipeline_table_c1:
        print("pipeline CALCULATION IS MATCHED")
    else:
        print("pipeline CALCULATION IS MIS-MATCHED")

    # gpper_calculation
    time.sleep(1)
    gpper_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[3]/td[2]").text
    gpper_modify_c1 = float(gpper_value_c1.strip("%"))
    round_gpper_c1 = round(gpper_modify_c1)
    gpper_table_c1 = (f"{round_gpper_c1}%")
    print("gpper value from table=", gpper_table_c1)
    round_gpper_calc_c1 = round(gp_per_calc_c1)
    gpper_result_calc_c1 = (f"{round_gpper_calc_c1}%")
    print("gpper value from calc=", gpper_result_calc_c1)
    if gpper_result_calc_c1 == gpper_table_c1:
        print("GP% CALCULATION IS MATCHED")
    else:
        print("GP% CALCULATION IS MIS-MATCHED")

    # rd_calculation
    time.sleep(1)
    rd_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[4]/td[2]").text
    rd_modify_c1 = float(rd_value_c1.strip("%"))
    round_rd_c1 = round(rd_modify_c1)
    rd_table_c1 = (f"{round_rd_c1}%")
    print("rd value from table=", rd_table_c1)
    round_rd_calc_c1 = round(rd_calc_c1)
    rd_result_calc_c1 = (f"{round_rd_calc_c1}%")
    print("rd value from calc=", rd_result_calc_c1)
    if rd_result_calc_c1 == rd_table_c1:
        print("RD% CALCULATION IS MATCHED")
    else:
        print("RD% CALCULATION IS MIS-MATCHED")

    # sm_calculation
    time.sleep(1)
    sm_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[5]/td[2]").text
    sm_modify_c1 = float(sm_value_c1.strip("%"))
    round_sm_c1 = round(sm_modify_c1)
    sm_table_c1 = (f"{round_sm_c1}%")
    print("sm value from table=", sm_table_c1)
    round_sm_calc_c1 = round(sm_calc_c1)
    sm_result_calc_c1 = (f"{round_sm_calc_c1}%")
    print("sm value from calc=", sm_result_calc_c1)
    if sm_result_calc_c1 == sm_table_c1:
        print("SM% CALCULATION IS MATCHED")
    else:
        print("SM% CALCULATION IS MIS-MATCHED")

    # ga_calculation
    time.sleep(1)
    ga_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[6]/td[2]").text
    ga_modify_c1 = float(ga_value_c1.strip("%"))
    round_ga_c1 = round(ga_modify_c1)
    ga_table_c1 = (f"{round_ga_c1}%")
    print("ga value from table=", ga_table_c1)
    round_ga_calc_c1 = round(ga_calc_c1)
    ga_result_calc_c1 = (f"{round_ga_calc_c1}%")
    print("ga value from calc=", ga_result_calc_c1)
    if ga_result_calc_c1 == ga_table_c1:
        print("GA% CALCULATION IS MATCHED")
    else:
        print("GA% CALCULATION IS MIS-MATCHED")

    # ebitda_calculation
    time.sleep(1)
    ebitda_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[7]/td[2]").text
    ebitda_modify_c1 = float(ebitda_value_c1.strip("%"))
    round_ebitda_c1 = round(ebitda_modify_c1)
    ebitda_table_c1 = (f"{round_ebitda_c1}%")
    print("ebitda value from table=", ebitda_table_c1)
    round_ebitda_calc_c1 = round(ebitda_calc_c1)
    ebitda_result_calc_c1 = (f"{round_ebitda_calc_c1}%")
    print("ebitda value from calc=", ebitda_result_calc_c1)
    if ebitda_result_calc_c1 == ebitda_table_c1:
        print("EBITDA CALCULATION IS MATCHED")
    else:
        print("EBITDA CALCULATION IS MIS-MATCHED")

    # cash_runway_calculation
    time.sleep(1)
    cash_runway_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[8]/td[2]").text
    cash_runway_modify_c1 = float(cash_runway_value_c1.strip("%"))
    round_cash_runway_c1 = round(cash_runway_modify_c1)
    cash_runway_table_c1 = (f"{round_cash_runway_c1}%")
    print("cash_runway value from table=", cash_runway_table_c1)
    round_cash_runway_calc_c1 = round(cash_runway_calc_c1)
    cash_runway_result_calc_c1 = (f"{round_cash_runway_calc_c1}%")
    print("cash_runway value from calc=", cash_runway_result_calc_c1)
    if cash_runway_result_calc_c1 == cash_runway_table_c1:
        print("CASH RUNWAY CALCULATION IS MATCHED")
    else:
        print("CASH RUNWAY CALCULATION IS MIS-MATCHED")

    # revee_calculation
    time.sleep(1)
    revee_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[9]/td[2]").text
    revee_table_c1 = revee_value_c1
    print("revee value from table=", revee_table_c1)
    rev_and_ee_round=round(rev_and_ee_calc_c1)
    revee_result_calc_c1 = "$ {:,}".format(rev_and_ee_round)
    print("revee value from calc=", revee_result_calc_c1)
    if revee_result_calc_c1 == revee_table_c1:
        print("REV&EE CALCULATION IS MATCHED")
    else:
        print("REV$EE CALCULATION IS MIS-MATCHED")

    # cust_churn_calculation
    time.sleep(1)
    cust_churn_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[10]/td[2]").text
    cust_churn_modify_c1 = float(cust_churn_value_c1.strip("%"))
    round_cust_churn_c1 = round(cust_churn_modify_c1)
    cust_churn_table_c1 = (f"{round_cust_churn_c1}%")
    print("cust_churn value from table=", cust_churn_table_c1)
    round_cust_churn_calc_c1 = round(cust_churn_calc_c1)
    cust_churn_result_calc_c1 = (f"{round_cust_churn_calc_c1}%")
    print("cust_churn value from calc=", cust_churn_result_calc_c1)
    if cust_churn_result_calc_c1 == cust_churn_table_c1:
        print("CUST CHURN CALCULATION IS MATCHED")
    else:
        print("CUSR CHURN CALCULATION IS MIS-MATCHED")

    # break_even_calculation
    time.sleep(1)
    break_even_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[11]/td[2]").text
    break_even_table_c1 = break_even_value_c1
    print("break_even value from table=", break_even_table_c1)
    round_break_even_calc_c1 = round(break_even_calc_c1)
    break_even_result_calc_c1 = "$ {:,}".format(round_break_even_calc_c1)
    print("break_even value from calc=", break_even_result_calc_c1)
    if break_even_result_calc_c1 == break_even_table_c1:
        print("BREAK EVEN CALCULATION IS MATCHED")
    else:
        print("BREAK EVEN CALCULATION IS MIS-MATCHED")

    # ltc_cac_calculation
    time.sleep(1)
    ltc_cac_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[12]/td[2]").text
    ltc_cac_modify_c1 = float(ltc_cac_value_c1.strip("%"))
    round_ltc_cac_c1 = round(ltc_cac_modify_c1)
    ltc_cac_table_c1 = (f"{round_ltc_cac_c1}%")
    print("ltc_cac value from table=", ltc_cac_table_c1)
    round_ltc_cac_calc_c1 = round(ltc_cac_calc_c1)
    ltc_cac_result_calc_c1 = (f"{round_ltc_cac_calc_c1}%")
    print("ltc_cac value from calc=", ltc_cac_result_calc_c1)
    if ltc_cac_result_calc_c1 == ltc_cac_table_c1:
        print("LTC:CAC CALCULATION IS MATCHED")
    else:
        print("LTC:CAC CALCULATION IS MIS-MATCHED")


    # current_ratio_calculation
    time.sleep(1)
    current_ratio_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[13]/td[2]").text
    current_ratio_modify_c1 = float(current_ratio_value_c1.strip("%"))
    round_current_ratio_c1 = round(current_ratio_modify_c1)
    current_ratio_table_c1 = (f"{round_current_ratio_c1}%")
    print("current_ratio value from table=", current_ratio_table_c1)
    round_current_ratio_calc_c1 = round(current_ratio_calc_c1)
    current_ratio_result_calc_c1 = (f"{round_current_ratio_calc_c1}%")
    print("current_ratio value from calc=", current_ratio_result_calc_c1)
    if current_ratio_result_calc_c1 == current_ratio_table_c1:
        print("CURRENT RATIO CALCULATION IS MATCHED")
    else:
        print("CURRENT RATIO CALCULATION IS MIS-MATCHED")

    # ee_churn_calculation
    time.sleep(1)
    ee_churn_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[14]/td[2]").text
    ee_churn_modify_c1 = float(ee_churn_value_c1.strip("%"))
    round_ee_churn_c1 = round(ee_churn_modify_c1)
    ee_churn_table_c1 = (f"{round_ee_churn_c1}%")
    print("ee_churn value from table=", ee_churn_table_c1)
    round_ee_churn_calc_c1 = round(ee_churn_calc_c1)
    ee_churn_result_calc_c1 = (f"{round_ee_churn_calc_c1}%")
    print("ee_churn value from calc=", ee_churn_result_calc_c1)
    if ee_churn_result_calc_c1 == ee_churn_table_c1:
        print("EECHURN CALCULATION IS MATCHED")
    else:
        print("EECHURN CALCULATION IS MIS-MATCHED")

    # opcash_flow_calculation
    time.sleep(1)
    opcash_flow_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[15]/td[2]").text
    opcash_flow_table_c1 = opcash_flow_value_c1
    print("opcash_flow value from table=", opcash_flow_table_c1)
    opcash_flow_result_calc_c1 = "$ {:,}".format(op_cashflow_calc_c1)
    print("opcash_flow value from calc=", opcash_flow_result_calc_c1)
    if opcash_flow_result_calc_c1 == opcash_flow_table_c1:
        print("OP CASHFLOW CALCULATION IS MATCHED")
    else:
        print("OP CASHFLOW CALCULATION IS MIS-MATCHED")

    # ar_dso_calculation
    time.sleep(1)
    ar_dso_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[16]/td[2]").text
    ar_dso_modify_c1 = float(ar_dso_value_c1.strip("%"))
    round_ar_dso_c1 = round(ar_dso_modify_c1)
    ar_dso_table_c1 = (f"{round_ar_dso_c1}%")
    print("ar_dso value from table=", ar_dso_table_c1)
    round_ar_dso_calc_c1 = round(ar_dso_calc_c1)
    ar_dso_result_calc_c1 = (f"{round_ar_dso_calc_c1}%")
    print("ar_dso value from calc=", ar_dso_result_calc_c1)
    if ar_dso_result_calc_c1 == ar_dso_table_c1:
        print("AR/DSO CALCULATION IS MATCHED")
    else:
        print("AR/DSO CALCULATION IS MIS-MATCHED")

    # ruleof40_calculation
    time.sleep(1)
    ruleof40_value_c1 = driver.find_element(By.XPATH, "//table/tbody/tr[17]/td[2]").text
    ruleof40_modify_c1 = float(ruleof40_value_c1.strip("%"))
    round_ruleof40_c1 = round(ruleof40_modify_c1)
    ruleof40_table_c1 = (f"{round_ruleof40_c1}%")
    print("ruleof40 value from table=", ruleof40_table_c1)
    round_ruleof40_calc_c1 = round(rule_of40_calc_c1)
    ruleof40_result_calc_c1 = (f"{round_ruleof40_calc_c1}%")
    print("ruleof40 value from calc=", ruleof40_result_calc_c1)
    if ruleof40_result_calc_c1 == ruleof40_table_c1:
        print("RULE OF 40 CALCULATION IS MATCHED")
    else:
        print("RULE OF 40 CALCULATION IS MIS-MATCHED")

    #BUSINESS SEGMENT
    print("___________BUSINESS SEGMENT__________")
    
    #cagr_business_segment calculation
    time.sleep(1)
    cagr_value_bs = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[3]").text
    cagr_modify_bs = float(cagr_value_bs.strip("%"))
    round_cagr_bs = round(cagr_modify_bs)
    cagr_table_bs = (f"{round_cagr_bs}%")
    print("CAGR value from table=", cagr_table_bs)
    round_cagr_calc_bs = round(business_segment_cagr)
    cagr_result_calc_bs = (f"{round_cagr_calc_bs}%")
    print("CAGR value from calc=", cagr_result_calc_bs)
    if cagr_result_calc_bs == cagr_table_bs:
        print("CAGR CALCULATION IS MATCHED IN BUSINESS SEGMENT")
    else:
        print("CAGR CALCULATION IS MIS-MATCHED IN BUSINESS SEGMENT")

    # pipelinecov_business_segment calculation
    time.sleep(1)
    pipelinecov_value_bs = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[3]").text
    pipelinecov_modify_bs = float(pipelinecov_value_bs.strip("%"))
    round_pipelinecov_bs = round(pipelinecov_modify_bs)
    pipelinecov_table_bs = (f"{round_pipelinecov_bs}%")
    print("pipelinecov value from table=", pipelinecov_table_bs)
    round_pipelinecov_calc_bs = round(business_segment_pipeline)
    pipelinecov_result_calc_bs = (f"{round_pipelinecov_calc_bs}%")
    print("pipelinecov value from calc=", pipelinecov_result_calc_bs)
    if pipelinecov_result_calc_bs == pipelinecov_table_bs:
        print("PIPELINE COV CALCULATION IS MATCHED IN BUSINESS SEGMENT")
    else:
        print("PIPELINE COV CALCULATION IS MIS-MATCHED IN BUSINESS SEGMENT")

    # gp_per_business_segment calculation
    time.sleep(1)
    gp_per_value_bs = driver.find_element(By.XPATH, "//table/tbody/tr[3]/td[3]").text
    gp_per_modify_bs = float(gp_per_value_bs.strip("%"))
    round_gp_per_bs = round(gp_per_modify_bs)
    gp_per_table_bs = (f"{round_gp_per_bs}%")
    print("gp_per value from table=", gp_per_table_bs)
    round_gp_per_calc_bs = round(business_segment_gpper)
    gp_per_result_calc_bs = (f"{round_gp_per_calc_bs}%")
    print("gp_per value from calc=", gp_per_result_calc_bs)
    if gp_per_result_calc_bs == gp_per_table_bs:
        print("GP% CALCULATION IS MATCHED IN BUSINESS SEGMENT")
    else:
        print("GP% CALCULATION IS MIS-MATCHED IN BUSINESS SEGMENT")

    # rd_business_segment calculation
    time.sleep(1)
    rd_value_bs = driver.find_element(By.XPATH, "//table/tbody/tr[4]/td[3]").text
    rd_modify_bs = float(rd_value_bs.strip("%"))
    round_rd_bs = round(rd_modify_bs)
    rd_table_bs = (f"{round_rd_bs}%")
    print("rd value from table=", rd_table_bs)
    round_rd_calc_bs = round(business_segment_rd)
    rd_result_calc_bs = (f"{round_rd_calc_bs}%")
    print("rd value from calc=", rd_result_calc_bs)
    if rd_result_calc_bs == rd_table_bs:
        print("RD CALCULATION IS MATCHED IN BUSINESS SEGMENT")
    else:
        print("RD CALCULATION IS MIS-MATCHED IN BUSINESS SEGMENT")

    # sm_business_segment calculation
    time.sleep(1)
    sm_value_bs = driver.find_element(By.XPATH, "//table/tbody/tr[5]/td[3]").text
    sm_modify_bs = float(sm_value_bs.strip("%"))
    round_sm_bs = round(sm_modify_bs)
    sm_table_bs = (f"{round_sm_bs}%")
    print("sm value from table=", sm_table_bs)
    round_sm_calc_bs = round(business_segment_sm)
    sm_result_calc_bs = (f"{round_sm_calc_bs}%")
    print("sm value from calc=", sm_result_calc_bs)
    if sm_result_calc_bs == sm_table_bs:
        print("SM CALCULATION IS MATCHED IN BUSINESS SEGMENT")
    else:
        print("SM CALCULATION IS MIS-MATCHED IN BUSINESS SEGMENT")

    # ga_business_segment calculation
    time.sleep(1)
    ga_value_bs = driver.find_element(By.XPATH, "//table/tbody/tr[6]/td[3]").text
    ga_modify_bs = float(ga_value_bs.strip("%"))
    round_ga_bs = round(ga_modify_bs)
    ga_table_bs = (f"{round_ga_bs}%")
    print("ga value from table=", ga_table_bs)
    round_ga_calc_bs = round(business_segment_ga)
    ga_result_calc_bs = (f"{round_ga_calc_bs}%")
    print("ga value from calc=", ga_result_calc_bs)
    if ga_result_calc_bs == ga_table_bs:
        print("GA CALCULATION IS MATCHED IN BUSINESS SEGMENT")
    else:
        print("GA CALCULATION IS MIS-MATCHED IN BUSINESS SEGMENT")

    # ebitda_business_segment calculation
    time.sleep(1)
    ebitda_value_bs = driver.find_element(By.XPATH, "//table/tbody/tr[7]/td[3]").text
    ebitda_modify_bs = float(ebitda_value_bs.strip("%"))
    round_ebitda_bs = round(ebitda_modify_bs)
    ebitda_table_bs = (f"{round_ebitda_bs}%")
    print("ebitda value from table=", ebitda_table_bs)
    round_ebitda_calc_bs = round(business_segment_ebitda)
    ebitda_result_calc_bs = (f"{round_ebitda_calc_bs}%")
    print("ebitda value from calc=", ebitda_result_calc_bs)
    if ebitda_result_calc_bs == ebitda_table_bs:
        print("ebitda CALCULATION IS MATCHED IN BUSINESS SEGMENT")
    else:
        print("ebitda CALCULATION IS MIS-MATCHED IN BUSINESS SEGMENT")

    # cash_runway_business_segment calculation
    time.sleep(1)
    cash_runway_value_bs = driver.find_element(By.XPATH, "//table/tbody/tr[8]/td[3]").text
    cash_runway_modify_bs = float(cash_runway_value_bs.strip("%"))
    round_cash_runway_bs = round(cash_runway_modify_bs)
    cash_runway_table_bs = (f"{round_cash_runway_bs}%")
    print("cash_runway value from table=", cash_runway_table_bs)
    round_cash_runway_calc_bs = round(business_segment_cashrunway)
    cash_runway_result_calc_bs = (f"{round_cash_runway_calc_bs}%")
    print("cash_runway value from calc=", cash_runway_result_calc_bs)
    if cash_runway_result_calc_bs == cash_runway_table_bs:
        print("cash_runway CALCULATION IS MATCHED IN BUSINESS SEGMENT")
    else:
        print("cash_runway CALCULATION IS MIS-MATCHED IN BUSINESS SEGMENT")


"""

   
    # business SEGMENT
    print("----business CALCULATION------")
    # cagr_calculation
    time.sleep(1)
    cagr = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[3]")
    cagr_value = cagr.text
    print("value from table:", cagr_value)
    cagr_calc = round(business_segment_cagr, 1)
    cagr_calc = (f"{cagr_calc}%")
    print("value from calc", cagr_calc)
    if cagr_calc == cagr_value:
        print("CAGR CALCULATION IS MATCHED WITH business SEGMENT")
    else:
        print("CAGR CALCULATION IS MIS-MATCHED WITH business SEGMENT")

    # pipelinecov_calculation
    time.sleep(1)
    pipeline = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[3]")
    pipelinecov_value = pipeline.text
    print("value from table:", pipelinecov_value)
    # pipeline_cov_calc=round(pipeline_cov_calc)
    pipeline_cov_calc = (f"{business_segment_pipeline}%")
    print("Value from Calculation:", pipeline_cov_calc)
    if pipelinecov_value == pipeline_cov_calc:
        print("PIPELINE CALCULATION IS MATCHED")
    else:
        print("PIPELINE CALCULATION IS MISMATCHED")

    # gppercentage
    time.sleep(1)
    gp = driver.find_element(By.XPATH, "//table/tbody/tr[3]/td[3]")
    gp_value = gp.text
    print("GP PERCENTAGE from table:", gp_value)
    gp_per_calc_c2 = round(business_segment_gpper, 1)
    gp_per_calc_c2 = (f"{gp_per_calc_c2}%")
    print("GP% from calculation:", gp_per_calc_c2)
    if gp_value == gp_per_calc_c2:
        print("GP% % CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("GP% CALCULATION MIS-MATCHED WITH business SEGMENT")

    # rd% calculation
    rd = driver.find_element(By.XPATH, "//table/tbody/tr[4]/td[3]")
    rd_value = rd.text
    print("RD% from table:", rd_value)
    rd_calc = round(business_segment_rd, 1)
    rd_calc = (f"{rd_calc}%")
    print("RD% Value from calculation", rd_calc)
    if rd_calc == rd_value:
        print("RD CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("RD CALCULATION MIS-MATCHED WITH business SEGMENT")

    # sm% calculation
    sm = driver.find_element(By.XPATH, "//table/tbody/tr[5]/td[3]")
    sm_value = sm.text
    print("SM% from table:", sm_value)
    sm_calc = round(business_segment_sm, 1)
    sm_calc = (f"{sm_calc}%")
    print("SM% value from calculation:", sm_calc)
    if sm_value == sm_calc:
        print("SM% CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("SM% CALCULATION MIS-MATCHED WITH business SEGMENT")

    # g&a calculation
    ga = driver.find_element(By.XPATH, "//table/tbody/tr[6]/td[3]")
    ga_value = ga.text
    print("GA value from table:", ga_value)
    ga_calc = round(business_segment_ga, 1)
    ga_calc = (f"{ga_calc}%")
    print("GA value from calculation:", ga_calc)
    if ga_value == ga_calc:
        print("GA CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("GA CALCULATION MIS_MATCHED WITH business SEGMENT")

    # ebitda calculation
    ebitdaper = driver.find_element(By.XPATH, "//table/tbody/tr[7]/td[3]")
    ebitda_value = ebitdaper.text
    print("EBITDA from table:", ebitda_value)
    ebitda_calc = round(business_segment_ebitda, 1)
    ebitda_calc = (f"{ebitda_calc}%")
    print("EBITDA from calculation:", ebitda_calc)
    if ebitda_value == ebitda_calc:
        print("EBITDA CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("EBITDA CALCULATION MIS_MATCHED WITH business SEGMENT")

    # cashruway calculation
    cashrunway = driver.find_element(By.XPATH, "//table/tbody/tr[8]/td[3]")
    cashrunway_value = cashrunway.text
    print("CASHRUNWAY from table:", cashrunway_value)
    cash_runway_calc = round(business_segment_cashrunway, 1)
    cash_runway_calc = (f"{cash_runway_calc}%")
    print("CASHRUNWAY from calculation:", cash_runway_calc)
    if cashrunway_value == cash_runway_calc:
        print("CASHRUNWAY CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("CASHRUNWAY CALCULATION MIS-MATCHED WITH business SEGMENT")

    # revandee calculation
    rev_and_ee = driver.find_element(By.XPATH, "//table/tbody/tr[9]/td[3]")
    rev_and_ee_value = rev_and_ee.text
    print("REV AND EE from table:", rev_and_ee_value)
    rev_and_ee_calc = round(business_segment_rev_ee)
    rev_and_ee_calc = "{:,}".format(rev_and_ee_calc)
    rev_and_ee_calc = (f"$ {rev_and_ee_calc}")
    print("REV AND EE from calculation:", rev_and_ee_calc)
    if rev_and_ee_value == rev_and_ee_calc:
        print("REV AND EE CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("REV AND EE CALCULATION MIS_MATCHED WITH business SEGMENT")

    # custchurn calculation
    custchurn = driver.find_element(By.XPATH, "//table/tbody/tr[10]/td[3]")
    custchurn_value = custchurn.text
    print("CUSTCHURN from table:", custchurn_value)
    cust_churn_calc_c2 = round(business_segment_custchurn, 1)
    cust_churn_calc_2 = (f"{cust_churn_calc_c2}%")
    print("CUSTCHURN from calculation:", cust_churn_calc)
    if custchurn_value == cust_churn_calc:
        print("CUSTOMERCHURN VALUE MATCHED WITH business SEGMENT")
    else:
        print("CUSTOMERCHURN VALUE MIS-MATCHED WITH business SEGMENT")

    # breakeven calculation
    breakeven = driver.find_element(By.XPATH, "//table/tbody/tr[11]/td[3]")
    breakeven_value = breakeven.text
    print("BREAKEVEN from table", breakeven_value)
    break_even_calc = round(business_segment_breakeven)
    break_even_calc = "{:,}".format(break_even_calc)
    break_even_calc = (f"$ {break_even_calc}")
    print("BREAKEVEN from calculation:", break_even_calc)
    if breakeven_value == break_even_calc:
        print("BREAKEVEN CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("BREAKEVEN CALCULATION MIS-MATCHED WITH business SEGMENT")

    # ltc:cac calculation
    ltc_cac = driver.find_element(By.XPATH, "//table/tbody/tr[12]/td[3]")
    ltc_cac_value = ltc_cac.text
    print("LTC CAC from table:", ltc_cac_value)
    ltc_cac_calc = round(business_segment_ltv_cac, 1)
    ltc_cac_calc = (f"{ltc_cac_calc}%")
    print("LTC CAC from calculation:", ltc_cac_calc)
    if ltc_cac_value == ltc_cac_calc:
        print("LTC:CAC CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("LTC:CAC CALCULATION MIS_MATCHED WITH business SEGMENT")

    # currentration calculation
    currentratio = driver.find_element(By.XPATH, "//table/tbody/tr[13]/td[3]")
    currentratio_value = currentratio.text
    print("CURRENT RATIO from table:", currentratio_value)
    current_ratio_calc = round(business_segment_current_ratio, 1)
    current_ratio_calc = (f"{current_ratio_calc}%")
    print("CURRENT RATIO from calculation", current_ratio_calc)
    if currentratio_value == current_ratio_calc:
        print("CURRENT RATIO CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("CURRENT RATIO CALCULATION MIS-MATCHED WITH business SEGMENT")

    # eechurn calculation
    eechurn = driver.find_element(By.XPATH, "//table/tbody/tr[14]/td[3]")
    eechurn_value = eechurn.text
    print("EE CHURN from table:", eechurn_value)
    ee_churn_calc = round(business_segment_eechurn)
    ee_churn_calc = (f"{ee_churn_calc}%")
    print("EE CHURN calculation:", ee_churn_calc)
    if eechurn_value == ee_churn_calc:
        print("EECHURN CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("EECHURN CALCULATION MIS_MATCHED WITH business SEGMENT")

    # opcashflow calculation
    opcashflow = driver.find_element(By.XPATH, "//table/tbody/tr[15]/td[3]")
    opcashflow_value = opcashflow.text
    print("OP CASH FLOW from table", opcashflow_value)
    op_cashflow_calc = round(business_segment_opcashflow)
    op_cashflow_calc = "{:,}".format(op_cashflow_calc)
    op_cashflow_calc = (f"$ {op_cashflow_calc}")
    print("OP CASH FLOW from calculation", op_cashflow_calc)
    if opcashflow_value == op_cashflow_calc:
        print("OPCASHFLOW CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("OPCASHFLOW CALCULATION MIS-MATCHED WITH business SEGMENT")

    # ardso calculation
    ardso = driver.find_element(By.XPATH, "//table/tbody/tr[16]/td[2]")
    ardso_value = ardso.text
    print("AR DSO from table:", ardso_value)
    ar_dso_calc = round(business_segment_ardso)
    ar_dso_calc = (f"{ar_dso_calc}%")
    print("AR DSO from calculation:", ar_dso_calc)
    if ardso_value == ar_dso_calc:
        print("ARDSO CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("ARDSO CALCULATION MISMATCHED WITH business SEGMENT")

    # ruleof40 calculation
    ruleof40 = driver.find_element(By.XPATH, "//table/tbody/tr[17]/td[3]")
    ruleof40_value = ruleof40.text
    print("RULE OF 40 from table", ruleof40_value)
    rule_of40_calc = round(business_segment_rule40, 1)
    rule_of40_calc = (f"{rule_of40_calc}%")
    print("RULE OF 40 from calculation:", rule_of40_calc)
    if ruleof40_value == rule_of40_calc:
        print("RULE OF 40 CALCULATION MATCHED WITH business SEGMENT")
    else:
        print("RULE OF 40 CALCULATION MIS_MATCHED WITH business SEGMENT")

"""
em_login()
em_metric()

