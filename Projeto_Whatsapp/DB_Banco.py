# myscript.py

import cx_Oracle
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Mensagem = []

# -------------------------------------------------
#   Realizando consulta com o Banco de Dados
# -------------------------------------------------

dsn_tns = cx_Oracle.makedsn('192.168.3.170', '1521', service_name='TMHML') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'andre_francisco', password='Francisco4', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute("SELECT * FROM TMHML.SC5010 SC5 WHERE SC5.C5_NUM = '000001'") # use triple quotes if you want to spread your query across multiple lines
for row in c:
    # print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc. 
    (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc. 
    Mensagem += ('Filial: ',row[0], '-', 'Pedido: ', row[1],'\n')
conn.close()


#Mensagem = ('client: ',row[5], '-', 'Loja: ', row[6])
MesagemLimpa = ''.join(Mensagem)

# -------------------------------------------------
#   Testando conexão com a rede
# -------------------------------------------------

import urllib.request

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
# test
print( 'connected' if connect() else 'no internet!' )


# -----# 

#Do not use this path that is extracted from "chrome://version/"
exec_path_driver = r"C:\Users\andre.francisco\AppData\Local\Programs\Python\Python310-32\Scripts\chromedriver"

chrome_options = webdriver.ChromeOptions();
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--start-maximized')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option('excludeSwitches', ['load-extension', 'enable-automation'])
chrome_options.add_argument(r'user-data-dir=C:\Users\andre.francisco\AppData\Local\Google\Chrome\User Data\Default')

driver = webdriver.Chrome(executable_path = exec_path_driver,chrome_options=chrome_options)

url = "https://web.whatsapp.com/send?phone=+5544998790822"
driver.get(url)

time.sleep(8) 

# --- #
Msg = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
SendMsga = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button/span'


# --- # 
driver.find_element_by_xpath(Msg).send_keys(MesagemLimpa)  #Mensagem a ser enviado!!
time.sleep(2)
driver.find_element_by_xpath(SendMsga).click()
time.sleep(9)
driver.quit()
