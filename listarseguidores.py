#pip install --> selenium, webdriver-manager, soup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# entrando no instagram
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.instagram.com/")
time.sleep(2)
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("seu login")
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("sua senha")
navegador.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
time.sleep(5)
navegador.get("https://www.instagram.com/digiteoinsta/followers/")




input() #para o código não fechar