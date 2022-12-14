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
   username= driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Email']")
   username.send_keys("calculation@devaxcel.com")

   time.sleep(1)
   password = driver.find_element(By.XPATH, "//input[@aria-label='Enter Your Password']")
   password.send_keys("1Qazxsw2@")

   time.sleep(1)
   signinbutton = driver.find_element(By.XPATH, "//button[@type = 'submit']")
   signinbutton.click()

   ignore_list = [NoSuchElementException, ElementNotSelectableException]
   wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=NoSuchElementException)
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
   metricoption = driver.find_elements(By.XPATH, "//div[@class='q-item__label']")
   print("options", len(metricoption))
   metricoption[0].click()

   # values assigned for client1
   previous_year_revenue = 12000000
   current_year_revenue = 15000000
   current_assests = 1562000
   current_liliability = 1200000
   quota = 4000000
   pipeline_cost = 5200000
   gross_profit = 13000000
   rd_cost = 3500000
   sm_cost = 2800000
   ga_cost = 1900000
   ebitda = 1100000
   cash_balance = 1200000
   burn_rate = 40000
   employee_boy = 212
   employee_eoy = 248
   customer_churn = 235000
   fixed_costs = 8000000
   life_time_value = 25000
   customer_acquisition_cost = 4000
   ar_boy_and_boq = 895000
   ar_eoy_and_eoq = 1100000
   ee_churn = 22
   op_cash_flow = 125000

   # calculation  of client1
   cagr_calc = ((current_year_revenue - previous_year_revenue) / previous_year_revenue) * 100
   pipeline_cov_calc = (pipeline_cost / quota)
   gp_per_calc = (gross_profit / current_year_revenue) * 100
   rd_calc = (rd_cost / current_year_revenue) * 100
   sm_calc = (sm_cost / current_year_revenue) * 100
   ga_calc = (ga_cost / current_year_revenue) * 100
   ebitda_calc = (ebitda / current_year_revenue) * 100
   cash_runway_calc = (cash_balance / burn_rate)
   rev_and_ee_calc = current_year_revenue / ((employee_boy + employee_eoy) / 2)
   cust_churn_calc = (customer_churn / current_year_revenue) * 100
   break_even_calc = (fixed_costs / gp_per_calc) * 100
   ltc_cac_calc = (life_time_value / customer_acquisition_cost)
   current_ratio_calc = (current_assests / current_liliability)
   ee_churn_calc = ee_churn
   op_cashflow_calc = op_cash_flow
   ar_dso_calc = (current_year_revenue // ((ar_boy_and_boq + ar_eoy_and_eoq) / 2))
   rule_of40_calc = cagr_calc + ebitda_calc

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
   ga_cost_c2  = 1900000
   ebitda_c2 = 1100000
   cash_balance_c2 = 1400000
   burn_rate_c2 = 40000
   employee_boy_c2 = 212
   employee_eoy_c2 = 248
   customer_churn_c2 = 235000
   fixed_costs_c2 = 8000000
   life_time_value_c2 = 25000
   customer_acquisition_cost_c2 = 4000
   ar_boy_and_boq_c2= 895000
   ar_eoy_and_eoq_c2 = 1100000
   ee_churn_c2 = 32
   op_cash_flow_c2 = 105000

   # calculation of client2
   cagr_calc_c2 = ((current_year_revenue_c2 - previous_year_revenue_c2) / previous_year_revenue_c2) * 100
   pipeline_cov_calc_c2 = (pipeline_cost_c2 / quota_c2)
   gp_per_calc_c2 = (gross_profit_c2 / current_year_revenue_c2) * 100
   rd_calc_c2 = (rd_cost_c2 / current_year_revenue_c2) * 100
   sm_calc_c2 = (sm_cost_c2 / current_year_revenue_c2) * 100
   ga_calc_c2= (ga_cost_c2 / current_year_revenue_c2) * 100
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
   rule_of40_calc_c2 = cagr_calc + ebitda_calc_c2

   #Buissness segment calculation
   buissness_segment_cagr=(cagr_calc+cagr_calc_c2)/2
   buissness_segment_pipeline=(pipeline_cov_calc+pipeline_cov_calc_c2)/2
   buissness_segment_gpper=(gp_per_calc+gp_per_calc_c2)/2
   buissness_segment_rd=(rd_calc+rd_calc_c2)/2
   buissness_segment_sm=(sm_calc+sm_calc_c2)/2
   buissness_segment_ga=(ga_calc+ga_calc_c2)/2
   buissness_segment_ebitda=(ebitda_calc+ebitda_calc_c2)/2
   buissness_segment_cashrunway=(cash_runway_calc+cash_runway_calc_c2)/2
   buissness_segment_rev_ee=(rev_and_ee_calc+rev_and_ee_calc_c2)/2
   buissness_segment_custchurn=(cust_churn_calc+cust_churn_calc_c2)/2
   buissness_segment_breakeven=(break_even_calc+break_even_calc_c2)/2
   buissness_segment_ltv_cac=(ltc_cac_calc+ltc_cac_calc_c2)/2
   buissness_segment_current_ratio=(current_ratio_calc+current_ratio_calc_c2)/2
   buissness_segment_eechurn=(ee_churn_calc+ee_churn_calc_c2)/2
   buissness_segment_opcashflow=(op_cashflow_calc+op_cashflow_calc_c2)/2
   buissness_segment_ardso=(ar_dso_calc+ar_dso_calc_c2)/2
   buissness_segment_rule40=(rule_of40_calc+rule_of40_calc_c2)/2
   
#RATIO
   print("----RATIO CALCULATION---- FIRST CLIENT")
   #cagr_calculation
   time.sleep(1)
   cagr = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[2]")
   cagr_value = cagr.text
   print("value from table:", cagr_value)
   cagr_calc = round(cagr_calc)
   cagr_calc = (f"{cagr_calc}%")
   print("value from calc", cagr_value)
   print(cagr_calc)
   if cagr_calc == cagr_value:
       print("CAGR CALCULATION IS MATCHED")
   else:
       print("CAGR CALCULATION IS MIS-MATCHED")

   #pipelinecov_calculation
   time.sleep(1)
   pipeline=driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[2]")
   pipelinecov_value=pipeline.text
   print("value from table:",pipelinecov_value)
   #pipeline_cov_calc=round(pipeline_cov_calc)
   pipeline_cov_calc=(f"{pipeline_cov_calc}%")
   print("Value from Calculation:",pipeline_cov_calc)
   if pipelinecov_value == pipeline_cov_calc:
       print("PIPELINE CALCULATION IS MATCHED")
   else:
       print("PIPELINE CALCULATION IS MISMATCHED")

   #gppercentage
   time.sleep(1)
   gp = driver.find_element(By.XPATH,"//table/tbody/tr[3]/td[2]")
   gp_value=gp.text
   print("GP PERCENTAGE from table:",gp_value)
   gp_per_calc=round(gp_per_calc,1)
   gp_per_calc=(f"{gp_per_calc}%")
   print("GP% from calculation:",gp_per_calc)
   if gp_value==gp_per_calc:
       print("GP% % CALCULATION MATCHED")
   else:
       print("GP% CALCULATION MIS-MATCHED")

   #rd% calculation
   rd=driver.find_element(By.XPATH,"//table/tbody/tr[4]/td[2]")
   rd_value=rd.text
   print("RD% from table:",rd_value)
   rd_calc=round(rd_calc,1)
   rd_calc=(f"{rd_calc}%")
   print("RD% Value from calculation",rd_calc)
   if rd_calc==rd_value:
       print("RD CALCULATION MATCHED")
   else:
       print("RD CALCULATION MIS-MATCHED")

   #sm% calculation
   sm=driver.find_element(By.XPATH,"//table/tbody/tr[5]/td[2]")
   sm_value=sm.text
   print("SM% from table:",sm_value)
   sm_calc=round(sm_calc,1)
   sm_calc=(f"{sm_calc}%")
   print("SM% value from calculation:",sm_calc)
   if sm_value==sm_calc:
       print("SM% CALCULATION MATCHED")
   else:
       print("SM% CALCULATION MISMATCHED")

   #g&a calculation
   ga=driver.find_element(By.XPATH,"//table/tbody/tr[6]/td[2]")
   ga_value=ga.text
   print("GA value from table:",ga_value)
   ga_calc=round(ga_calc,1)
   ga_calc=(f"{ga_calc}%")
   print("GA value from calculation:",ga_calc)
   if ga_value==ga_calc:
       print("GA CALCULATION MATCHED")
   else:
       print("GA CALCULATION MIS_MATCHED")

   #ebitda calculation
   ebitdaper=driver.find_element(By.XPATH,"//table/tbody/tr[7]/td[2]")
   ebitda_value=ebitdaper.text
   print("EBITDA from table:",ebitda_value)
   ebitda_calc=round(ebitda_calc,1)
   ebitda_calc=(f"{ebitda_calc}%")
   print("EBITDA from calculation:",ebitda_calc)
   if ebitda_value==ebitda_calc:
       print("EBITDA CALCULATION MATCHED")
   else:
       print("EBITDA CALCULATION MIS_MATCHED")

   #cashruway calculation
   cashrunway=driver.find_element(By.XPATH,"//table/tbody/tr[8]/td[2]")
   cashrunway_value=cashrunway.text
   print("CASHRUNWAY from table:",cashrunway_value)
   cash_runway_calc=round(cash_runway_calc)
   cash_runway_calc=(f"{cash_runway_calc}%")
   print("CASHRUNWAY from calculation:",cash_runway_calc)
   if cashrunway_value==cash_runway_calc:
       print("CASHRUNWAY CALCULATION MATCHED")
   else:
       print("CASHRUNWAY CALCULATION MIS-MATCHED")


   #revandee calculation
   rev_and_ee=driver.find_element(By.XPATH,"//table/tbody/tr[9]/td[2]")
   rev_and_ee_value=rev_and_ee.text
   print("REV AND EE from table:",rev_and_ee_value)
   rev_and_ee_calc=round(rev_and_ee_calc)
   rev_and_ee_calc="{:,}".format(rev_and_ee_calc)
   rev_and_ee_calc=(f"$ {rev_and_ee_calc}")
   print("REV AND EE from calculation:",rev_and_ee_calc)
   if rev_and_ee_value ==rev_and_ee_calc:
       print("REV AND EE CALCULATION MATCHED")
   else:
       print("REV AND EE CALCULATION MIS_MATCHED")

   #custchurn calculation
   custchurn=driver.find_element(By.XPATH,"//table/tbody/tr[10]/td[2]")
   custchurn_value=custchurn.text
   print("CUSTCHURN from table:",custchurn_value)
   cust_churn_calc=round(cust_churn_calc,1)
   cust_churn_calc=(f"{cust_churn_calc}%")
   print("CUSTCHURN from calculation:",cust_churn_calc)
   if custchurn_value==cust_churn_calc:
       print("CUSTOMERCHURN VALUE MATCHED")
   else:
       print("CUSTOMERCHURN VALUE MIS-MATCHED")

   #breakeven calculation
   breakeven=driver.find_element(By.XPATH,"//table/tbody/tr[11]/td[2]")
   breakeven_value=breakeven.text
   print("BREAKEVEN from table",breakeven_value)
   break_even_calc=round(break_even_calc)
   break_even_calc="{:,}".format(break_even_calc)
   break_even_calc=(f"$ {break_even_calc}")
   print("BREAKEVEN from calculation:",break_even_calc)
   if breakeven_value==break_even_calc:
       print("BREAKEVEN CALCULATION MATCHED")
   else:
       print("BREAKEVEN CALCULATION MIS-MATCHED")

   #ltc:cac calculation
   ltc_cac=driver.find_element(By.XPATH,"//table/tbody/tr[12]/td[2]")
   ltc_cac_value=ltc_cac.text
   print("LTC CAC from table:",ltc_cac_value)
   ltc_cac_calc=round(ltc_cac_calc,1)
   ltc_cac_calc=(f"{ltc_cac_calc}%")
   print("LTC CAC from calculation:",ltc_cac_calc)
   if ltc_cac_value==ltc_cac_calc:
       print("LTC:CAC CALCULATION MATCHED")
   else:
       print("LTC:CAC CALCULATION MIS_MATCHED")


   #currentration calculation
   currentratio=driver.find_element(By.XPATH,"//table/tbody/tr[13]/td[2]")
   currentratio_value=currentratio.text
   print("CURRENT RATIO from table:",currentratio_value)
   current_ratio_calc=round(current_ratio_calc,1)
   current_ratio_calc=(f"{current_ratio_calc}%")
   print("CURRENT RATIO from calculation",current_ratio_calc)
   if currentratio_value==current_ratio_calc:
       print("CURRENT RATIO CALCULATION MATCHED")
   else:
       print("CURRENT RATIO CALCULATION MIS-MATCHED")

   #eechurn calculation
   eechurn=driver.find_element(By.XPATH,"//table/tbody/tr[14]/td[2]")
   eechurn_value=eechurn.text
   print("EE CHURN from table:",eechurn_value)
   ee_churn_calc=round(ee_churn_calc)
   ee_churn_calc=(f"{ee_churn_calc}%")
   print("EE CHURN calculation:",ee_churn_calc)
   if eechurn_value==ee_churn_calc:
       print("EECHURN CALCULATION MATCHED")
   else:
       print("EECHURN CALCULATION MIS_MATCHED")

   #opcashflow calculation
   opcashflow=driver.find_element(By.XPATH,"//table/tbody/tr[15]/td[2]")
   opcashflow_value=opcashflow.text
   print("OP CASH FLOW from table",opcashflow_value)
   op_cashflow_calc=round(op_cashflow_calc)
   op_cashflow_calc="{:,}".format(op_cashflow_calc)
   op_cashflow_calc=(f"$ {op_cashflow_calc}")
   print("OP CASH FLOW from calculation",op_cashflow_calc)
   if opcashflow_value==op_cashflow_calc:
       print("OPCASHFLOW CALCULATION MATCHED")
   else:
       print("OPCASHFLOW CALCULATION MIS-MATCHED ")

   #ardso calculation
   ardso=driver.find_element(By.XPATH,"//table/tbody/tr[16]/td[2]")
   ardso_value=ardso.text
   print("AR DSO from table:",ardso_value)
   ar_dso_calc=round(ar_dso_calc)
   ar_dso_calc=(f"{ar_dso_calc}%")
   print("AR DSO from calculation:",ar_dso_calc)
   if ardso_value==ar_dso_calc:
       print("ARDSO CALCULATION MATCHED")
   else:
       print("ARDSO CALCULATION MISMATCHED")

   #ruleof40 calculation
   ruleof40=driver.find_element(By.XPATH,"//table/tbody/tr[17]/td[2]")
   ruleof40_value=ruleof40.text
   print("RULE OF 40 from table",ruleof40_value)
   rule_of40_calc=round(rule_of40_calc,1)
   rule_of40_calc=(f"{rule_of40_calc}%")
   print("RULE OF 40 from calculation:",rule_of40_calc)
   if ruleof40_value==rule_of40_calc:
       print("RULE OF 40 CALCULATION MATCHED")
   else:
       print("RULE OF 40 CALCULATION MIS_MATCHED")





   # BUISSNESS SEGMENT
   print("----BUISSNESS CALCULATION------")
   # cagr_calculation
   time.sleep(1)
   cagr = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[3]")
   cagr_value = cagr.text
   print("value from table:", cagr_value)
   cagr_calc = round(buissness_segment_cagr,1)
   cagr_calc = (f"{cagr_calc}%")
   print("value from calc", cagr_calc)
   if cagr_calc == cagr_value:
      print("CAGR CALCULATION IS MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("CAGR CALCULATION IS MIS-MATCHED WITH BUISSNESS SEGMENT")

   # pipelinecov_calculation
   time.sleep(1)
   pipeline = driver.find_element(By.XPATH, "//table/tbody/tr[2]/td[3]")
   pipelinecov_value = pipeline.text
   print("value from table:", pipelinecov_value)
   # pipeline_cov_calc=round(pipeline_cov_calc)
   pipeline_cov_calc = (f"{buissness_segment_pipeline}%")
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
   gp_per_calc_c2 = round(buissness_segment_gpper, 1)
   gp_per_calc_c2 = (f"{gp_per_calc_c2}%")
   print("GP% from calculation:", gp_per_calc_c2)
   if gp_value == gp_per_calc_c2:
      print("GP% % CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("GP% CALCULATION MIS-MATCHED WITH BUISSNESS SEGMENT")

   # rd% calculation
   rd = driver.find_element(By.XPATH, "//table/tbody/tr[4]/td[3]")
   rd_value = rd.text
   print("RD% from table:", rd_value)
   rd_calc = round(buissness_segment_rd, 1)
   rd_calc = (f"{rd_calc}%")
   print("RD% Value from calculation", rd_calc)
   if rd_calc == rd_value:
      print("RD CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("RD CALCULATION MIS-MATCHED WITH BUISSNESS SEGMENT")

   # sm% calculation
   sm = driver.find_element(By.XPATH, "//table/tbody/tr[5]/td[3]")
   sm_value = sm.text
   print("SM% from table:", sm_value)
   sm_calc = round(buissness_segment_sm, 1)
   sm_calc = (f"{sm_calc}%")
   print("SM% value from calculation:", sm_calc)
   if sm_value == sm_calc:
      print("SM% CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("SM% CALCULATION MIS-MATCHED WITH BUISSNESS SEGMENT")

   # g&a calculation
   ga = driver.find_element(By.XPATH, "//table/tbody/tr[6]/td[3]")
   ga_value = ga.text
   print("GA value from table:", ga_value)
   ga_calc = round(buissness_segment_ga, 1)
   ga_calc = (f"{ga_calc}%")
   print("GA value from calculation:", ga_calc)
   if ga_value == ga_calc:
      print("GA CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("GA CALCULATION MIS_MATCHED WITH BUISSNESS SEGMENT")

   # ebitda calculation
   ebitdaper = driver.find_element(By.XPATH, "//table/tbody/tr[7]/td[3]")
   ebitda_value = ebitdaper.text
   print("EBITDA from table:", ebitda_value)
   ebitda_calc = round(buissness_segment_ebitda, 1)
   ebitda_calc = (f"{ebitda_calc}%")
   print("EBITDA from calculation:", ebitda_calc)
   if ebitda_value == ebitda_calc:
      print("EBITDA CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("EBITDA CALCULATION MIS_MATCHED WITH BUISSNESS SEGMENT")

   # cashruway calculation
   cashrunway = driver.find_element(By.XPATH, "//table/tbody/tr[8]/td[3]")
   cashrunway_value = cashrunway.text
   print("CASHRUNWAY from table:", cashrunway_value)
   cash_runway_calc = round(buissness_segment_cashrunway,1)
   cash_runway_calc = (f"{cash_runway_calc}%")
   print("CASHRUNWAY from calculation:", cash_runway_calc)
   if cashrunway_value == cash_runway_calc:
      print("CASHRUNWAY CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("CASHRUNWAY CALCULATION MIS-MATCHED WITH BUISSNESS SEGMENT")

   # revandee calculation
   rev_and_ee = driver.find_element(By.XPATH, "//table/tbody/tr[9]/td[3]")
   rev_and_ee_value = rev_and_ee.text
   print("REV AND EE from table:", rev_and_ee_value)
   rev_and_ee_calc = round(buissness_segment_rev_ee)
   rev_and_ee_calc = "{:,}".format(rev_and_ee_calc)
   rev_and_ee_calc = (f"$ {rev_and_ee_calc}")
   print("REV AND EE from calculation:", rev_and_ee_calc)
   if rev_and_ee_value == rev_and_ee_calc:
      print("REV AND EE CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("REV AND EE CALCULATION MIS_MATCHED WITH BUISSNESS SEGMENT")

   # custchurn calculation
   custchurn = driver.find_element(By.XPATH, "//table/tbody/tr[10]/td[3]")
   custchurn_value = custchurn.text
   print("CUSTCHURN from table:", custchurn_value)
   cust_churn_calc_c2 = round(buissness_segment_custchurn, 1)
   cust_churn_calc_2 = (f"{cust_churn_calc_c2}%")
   print("CUSTCHURN from calculation:", cust_churn_calc)
   if custchurn_value == cust_churn_calc:
      print("CUSTOMERCHURN VALUE MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("CUSTOMERCHURN VALUE MIS-MATCHED WITH BUISSNESS SEGMENT")

   # breakeven calculation
   breakeven = driver.find_element(By.XPATH, "//table/tbody/tr[11]/td[3]")
   breakeven_value = breakeven.text
   print("BREAKEVEN from table", breakeven_value)
   break_even_calc = round(buissness_segment_breakeven)
   break_even_calc = "{:,}".format(break_even_calc)
   break_even_calc = (f"$ {break_even_calc}")
   print("BREAKEVEN from calculation:", break_even_calc)
   if breakeven_value == break_even_calc:
      print("BREAKEVEN CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("BREAKEVEN CALCULATION MIS-MATCHED WITH BUISSNESS SEGMENT")

   # ltc:cac calculation
   ltc_cac = driver.find_element(By.XPATH, "//table/tbody/tr[12]/td[3]")
   ltc_cac_value = ltc_cac.text
   print("LTC CAC from table:", ltc_cac_value)
   ltc_cac_calc = round(buissness_segment_ltv_cac, 1)
   ltc_cac_calc = (f"{ltc_cac_calc}%")
   print("LTC CAC from calculation:", ltc_cac_calc)
   if ltc_cac_value == ltc_cac_calc:
      print("LTC:CAC CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("LTC:CAC CALCULATION MIS_MATCHED WITH BUISSNESS SEGMENT")

   # currentration calculation
   currentratio = driver.find_element(By.XPATH, "//table/tbody/tr[13]/td[3]")
   currentratio_value = currentratio.text
   print("CURRENT RATIO from table:", currentratio_value)
   current_ratio_calc = round(buissness_segment_current_ratio, 1)
   current_ratio_calc = (f"{current_ratio_calc}%")
   print("CURRENT RATIO from calculation", current_ratio_calc)
   if currentratio_value == current_ratio_calc:
      print("CURRENT RATIO CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("CURRENT RATIO CALCULATION MIS-MATCHED WITH BUISSNESS SEGMENT")

   # eechurn calculation
   eechurn = driver.find_element(By.XPATH, "//table/tbody/tr[14]/td[3]")
   eechurn_value = eechurn.text
   print("EE CHURN from table:", eechurn_value)
   ee_churn_calc = round(buissness_segment_eechurn)
   ee_churn_calc = (f"{ee_churn_calc}%")
   print("EE CHURN calculation:", ee_churn_calc)
   if eechurn_value == ee_churn_calc:
      print("EECHURN CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("EECHURN CALCULATION MIS_MATCHED WITH BUISSNESS SEGMENT")

   # opcashflow calculation
   opcashflow = driver.find_element(By.XPATH, "//table/tbody/tr[15]/td[3]")
   opcashflow_value = opcashflow.text
   print("OP CASH FLOW from table", opcashflow_value)
   op_cashflow_calc = round(buissness_segment_opcashflow)
   op_cashflow_calc = "{:,}".format(op_cashflow_calc)
   op_cashflow_calc = (f"$ {op_cashflow_calc}")
   print("OP CASH FLOW from calculation", op_cashflow_calc)
   if opcashflow_value == op_cashflow_calc:
      print("OPCASHFLOW CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("OPCASHFLOW CALCULATION MIS-MATCHED WITH BUISSNESS SEGMENT")

   # ardso calculation
   ardso = driver.find_element(By.XPATH, "//table/tbody/tr[16]/td[2]")
   ardso_value = ardso.text
   print("AR DSO from table:", ardso_value)
   ar_dso_calc = round(buissness_segment_ardso)
   ar_dso_calc = (f"{ar_dso_calc}%")
   print("AR DSO from calculation:", ar_dso_calc)
   if ardso_value == ar_dso_calc:
      print("ARDSO CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("ARDSO CALCULATION MISMATCHED WITH BUISSNESS SEGMENT")

   # ruleof40 calculation
   ruleof40 = driver.find_element(By.XPATH, "//table/tbody/tr[17]/td[3]")
   ruleof40_value = ruleof40.text
   print("RULE OF 40 from table", ruleof40_value)
   rule_of40_calc = round(buissness_segment_rule40, 1)
   rule_of40_calc = (f"{rule_of40_calc}%")
   print("RULE OF 40 from calculation:", rule_of40_calc)
   if ruleof40_value == rule_of40_calc:
      print("RULE OF 40 CALCULATION MATCHED WITH BUISSNESS SEGMENT")
   else:
      print("RULE OF 40 CALCULATION MIS_MATCHED WITH BUISSNESS SEGMENT")




em_login()
em_metric()
