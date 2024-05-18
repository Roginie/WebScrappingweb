'''import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Configurar o serviço e as opções do Chrome
service = Service()
options = Options()
driver = webdriver.Chrome(service=service, options=options)

login = 'alanzoka75'
senha = 'Bill8828'
url = 'https://www.instagram.com/'

# Acessar a página de login
driver.get(url)
time.sleep(3)  # Esperar a página carregar

# Localizar os campos de login e senha
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password_input = driver.find_element(By.NAME, "password")

# Inserir as credenciais
username_input.send_keys(login)
password_input.send_keys(senha)

# Clicar no botão de login
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
login_button.click()

# Esperar a navegação pós-login
time.sleep(5)  # Ajustar conforme necessário

# Navegar para a página desejada
url2 = 'https://www.instagram.com/remamadragaorosa/reels/'
driver.get(url2)
time.sleep(5)  # Esperar a página carregar

# Coletar os links dos reels
links = driver.find_elements(By.CLASS_NAME, '_aajy')
print(len(links))

dados = []

for i in links:
    vizus = i.find_element(By.CLASS_NAME, 'html-span').text
    dados.append(vizus)
    # time.sleep(0.2)

print(links)
print(dados)

# Recarregar a página
url = 'https://www.instagram.com/remamadragaorosa/reels/'
driver.get(url)
time.sleep(10)

# Coletar os elementos dos reels
reels = driver.find_elements(By.CLASS_NAME, '_abq3')
print(len(reels))

if reels:
    a1 = reels[0].find_element(By.TAG_NAME, 'a')
    link3 = a1.get_attribute('href')
    driver.get(link3)
    time.sleep(5)
    meta_reel = driver.find_element(By.NAME, 'description')
    desc_reel = meta_reel.get_attribute('content')
    print(desc_reel)

# Fechar o navegador
driver.quit()'''
#____________________________________________________________________

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Configurar o serviço e as opções do Chrome
service = Service()
options = Options()
driver = webdriver.Chrome(service=service, options=options)

login = 'alanzoka75'
senha = 'Bill8828'
url = 'https://www.instagram.com/'

# Acessar a página de login
driver.get(url)
time.sleep(3)  # Esperar a página carregar

# Localizar os campos de login e senha
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password_input = driver.find_element(By.NAME, "password")

# Inserir as credenciais
username_input.send_keys(login)
password_input.send_keys(senha)

# Clicar no botão de login
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
login_button.click()

# Esperar a navegação pós-login
time.sleep(5)  # Ajustar conforme necessário

# Navegar para a página desejada
url2 = 'https://www.instagram.com/remamadragaorosa/reels/'
driver.get(url2)
time.sleep(5)  # Esperar a página carregar

# Coletar os links dos reels
reels = driver.find_elements(By.CLASS_NAME, '_aagw')  # Atualize conforme a classe real dos elementos
print(len(reels))

dados = []

for reel in reels:
    link = reel.find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.get(link)
    time.sleep(5)

    # Coletar o número de likes
    try:
        likes = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//section[@class="EDfFK ygqzn"]/div/div/button/span'))
        ).text
    except:
        likes = '0'

    # Coletar o número de comentários
    try:
        comments = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//ul[@class="Mr508"]/li/div/div/div[2]/span'))
        ).text
    except:
        comments = '0'

    dados.append({
        'link': link,
        'likes': likes,
        'comments': comments
    })

    # Voltar para a página de reels
    driver.back()
    time.sleep(5)

# Imprimir os dados coletados
print(dados)

# Fechar o navegador
driver.quit()

# Salvar os dados em um arquivo CSV
df = pd.DataFrame(dados)
df.to_csv('reels_data.csv', index=False)
