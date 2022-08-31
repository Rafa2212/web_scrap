from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
options.headless = True

browser = webdriver.Chrome('/Users/rafa22/dev/OLX/chromedriver', options=options)
browser.get("https://www.frf-ajf.ro/timis/meciuri-viitoare")

def check_exists_by_xpath(xpath):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

i = 4
p = 8

while i<80:
    if check_exists_by_xpath('//*[@id="page_wrapper"]/section/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[' + str(p) + ']') == False:
        i=i+1
    data = browser.find_element(By.XPATH, '//*[@id="page_wrapper"]/section/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[' + str(p) + ']')
    data=data.text
    if data.find("Tot R") !=-1:
        k=2
        while k<6:
            dat = browser.find_element(By.XPATH, '//*[@id="page_wrapper"]/section/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[' + str(k) + ']')
            dat=dat.text
            print(dat)
            k=k+1
    i=i+1