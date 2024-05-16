import time

import pandas as pd
#pip install pandas

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#pip install selenium

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

login = ''
senha = ''
url = 'https://www.instagram.com/'
inputs = driver.find_elements(By.TAG_NAME, 'input')

driver.get(url)
time.sleep(1)
driver.find_element(By.TAG_NAME, value="input").send_keys(login)
driver.find_element(By.NAME, value="password").send_keys(senha)
botoes = driver.find_elements(By.TAG_NAME, 'button')[:]
botoes[1].click()
time.sleep(2.5)

url2 = 'https://www.instagram.com/remamadragaorosa/reels/'
driver.get(url2)
time.sleep(5)

links = driver.find_elements(By.CLASS_NAME, '_aajy')
print(len(links))
dados = []

for i in links  :
    vizus = i.find_element(By.CLASS_NAME, 'html-span').text
    dados.append(vizus)
    #time.sleep(0.2)

print(links)
print(dados)