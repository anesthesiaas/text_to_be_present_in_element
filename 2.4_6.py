
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import math
try:    
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

   

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
   
    button = browser.find_element_by_id("book")
    button.click()
    
	
	
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_css_selector('[id="input_value"]')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_css_selector("[id='solve']")
    browser.execute_script("window.scrollBy(0,100);")
    button.click()
    
finally:
    
    time.sleep(10)
   
    browser.quit()