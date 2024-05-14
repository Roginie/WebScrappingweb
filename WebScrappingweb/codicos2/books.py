#nos queremos pegar todas os linques e em seguida gera uma data set
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://books.toscrape.com/index.html"

driver.get(url)
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, value="a")
print(links)
print(len(links))

#Os livros comesa no 54 e trermina em 92 de 2 em 2

x = driver.find_elements(By.TAG_NAME, value="a")[54].text
print(x)

y = driver.find_elements(By.TAG_NAME, value="a")[54].get_attribute("title")
print(y)

print(driver.find_elements(By.TAG_NAME, value="a")[54:94:2])

elementostitulos = driver.find_elements(By.TAG_NAME, value="a")[54:94:2]

listatitulos = [title.get_attribute("title") for title in elementostitulos]
print(listatitulos)

elementostitulos[1].click()
time.sleep(2)
stok = driver.find_element(By.CLASS_NAME, value="instock").text
time.sleep(2)
print(stok)