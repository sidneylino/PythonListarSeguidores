#pip install --> selenium, webdriver-manager, keyboard, pandas, openpyxl
import keyboard
import time
import openpyxl
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#obtendo informações do login e da coleta
email = input("digite seu login: ")
senha = input("digite a sua senha: ")
insta = input("digite o nome do insta que será coletado: ")
tempo = int(input("digite quantos minutos de coleta: (aproximadamente 250 seguidores em 1 minutos)"))
print("coletando o nome e o @\naguarde...")

# entrando no instagram
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.instagram.com/")
#logando no instagram e entrando no insta da coleta
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email)
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
time.sleep(10)
navegador.get(f"https://www.instagram.com/{insta}/followers/")
time.sleep(5)
#deixando usavel o scroll(rolagem) de seguidores
for i in range(0,5):
    time.sleep(1)
    keyboard.press('TAB')
#localizando a tabela onde estão os seguidores
tabela = navegador.find_elements(By.CSS_SELECTOR,'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano')

time.sleep(3)
#rolando a pagina dos seguidores para coleta-los
for t in range(0,tempo):
    for t in range(0,25):
        time.sleep(2)
        keyboard.press('End')
    print("coletando...")
    time.sleep(10)
#tranformando o elemento da pagina em texto
dados = []
for href in tabela:
    dados = href.text

#print(dados)
#separando os seguidores em variaveis numa lista
seguidores = dados.split("\n")
while "Seguir" in seguidores:
    seguidores.remove("Seguir")
#print(seguidores)
#criando um dataframe e transformando a lista em coluna
df = pd.DataFrame(zip(seguidores),columns=['seguidores'])
print(df)
#criando um excel com os seguidores
df.to_excel("teste.xlsx")




input() #para o código não fechar no pycharm