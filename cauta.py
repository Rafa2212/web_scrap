from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.olx.ro/d/timisoara/q-bicicleta/?search%5Bdist%5D=100&search%5Bphotos%5D=1&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D=900&search%5Bfilter_float_price:to%5D=2000&page=1")

p=1
i=15

while p<3:
    if i>45:
        p=p+1
        button = browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/li[' + str(p) + ']/a')
        browser.execute_script("arguments[0].click();", button)
        browser.get("https://www.olx.ro/d/timisoara/q-bicicleta/?search%5Bdist%5D=100&search%5Bphotos%5D=1&search%5Border%5D=created_at%3Adesc&search%5Bfilter_float_price%3Afrom%5D=900&search%5Bfilter_float_price%3Ato%5D=2000&page="+str(p))
        i=12
    i=str(i)
    data = browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/form/div[5]/div/div[2]/div[' + i + ']/a/div/div/div[2]/div[2]/p[1]')
    data = data.text
    if data.find("Azi") != -1 & data.find("Reactualizat") == -1:
        print("Da")
    i=int(i)
    i=i+1
