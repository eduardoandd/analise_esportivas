import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from lxml import html

endereco_time= {'al-hilal':'al-hilal/21895','al-taawoun':'al-taawoun/56021','al-ittihad':'al-ittihad/34315','al-ahli':'/al-ahli/34469','al-ettifaq':'al-ettifaq/34318','al-nassr':'al-nassr/23400','al-fateh':'al-fateh/56023','al-fayha':'al-fayha/168094','al-wehda':'al-wehda/32994','abha':'abha/168090','al-tai':'al-tai/168072','al-khaleej':'al-khaleej/167228','al-akhdood':'al-akhdood/336456','al-raed':'al-raed/56031','al-riyadh':'al-riyadh/168088','damac-fc':'damac-fc/204126','al-shabab':'al-shabab/34313','al-hazem':'al-hazem/168086'}

def procura_time(time:str):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    base_url='https://www.sofascore.com/team/football/'
    
    url= base_url + endereco_time[time]
    
    driver.get(url)
    
    soup =BeautifulSoup(driver.page_source, 'html.parser')
    
    conteudo = str(soup)
    
    estrutura = html.fromstring(conteudo)
    
    dicionario_de_dados={}
    
    for i in range(2,7):
        base_xpath= f'//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div[4]/div[3]/div[{i}]/div[2]/div[*]/'
        elemento_1 = estrutura.xpath(base_xpath + 'span[1]')
        elemento_2 = estrutura.xpath(base_xpath + 'span[2]')
        for dado in range(len(elemento_1)):
            if dado==0:
                dicionario_de_dados['Time'] = time.title()
            dicionario_de_dados[elemento_1[dado].text] =elemento_2[dado].text
            
    return dicionario_de_dados
            
            
        
    
    



