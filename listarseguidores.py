#pip install --> selenium, webdriver-manager
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# entrando no instagram
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.instagram.com/")
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("seu email")
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("sua senha")
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
time.sleep(5)
navegador.get("https://www.instagram.com/InstaDaListagem/followers/")
time.sleep(5)
tabela = navegador.find_elements(By.CSS_SELECTOR,'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano')

for href in tabela:
    print(href.text)



input() #para o código não fechar no pycharm