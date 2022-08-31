from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = "https://www.cargopedia.ro/preturi-carburanti-europa"
options = Options()
options.headless = True

browser = webdriver.Chrome('/Users/rafa22/dev/OLX/chromedriver', options=options)
browser.get(url)

benzina = browser.find_element(By.XPATH, '//*[@id="body"]/div/div/div/table/tbody/tr[1]/td[3]')
benzina = benzina.text
benzina = benzina.replace(",", ".")
benzina = float(benzina)

motorina = browser.find_element(By.XPATH, '//*[@id="body"]/div/div/div/table/tbody/tr[1]/td[5]')
motorina = motorina.text
motorina = motorina.replace(",", ".")
motorina = float(motorina)

combustibil = input("Benzina/Motorina: ")

distanta = input("Distanta in km parcursa:")
distanta = float(distanta)

cosum_mediu = input("Cosum mediu pe 100km: ")
cosum_mediu = float(cosum_mediu)

litri = distanta*cosum_mediu/100

if combustibil == "benzina":
    pret = round(litri*benzina)
    print("Pretul este: ", pret)
elif combustibil == "motorina":
    pret = round(litri*motorina)
    print("Pretul este: ", pret)
