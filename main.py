import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import plotly.graph_objects as go

endereco_time= {'al-hilal':'al-hilal/21895','al-taawoun':'al-taawoun/56021','al-ittihad':'al-ittihad/34315','al-ahli':'/al-ahli/34469','al-ettifaq':'al-ettifaq/34318','al-nassr':'al-nassr/23400','al-fateh':'al-fateh/56023','al-fayha':'al-fayha/168094','al-wehda':'al-wehda/32994','abha':'abha/168090','al-tai':'al-tai/168072','al-khaleej':'al-khaleej/167228','al-akhdood':'al-akhdood/336456','al-raed':'al-raed/56031','al-riyadh':'al-riyadh/168088','damac-fc':'damac-fc/204126','al-shabab':'al-shabab/34313','al-hazem':'al-hazem/168086'}

browser={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}


base_api='https://api.sofascore.com/api/v1/team/'
end_api='/statistics/overall'

def escolhe_time(time:str):
    lista_dados=  []
    cont_url_list=0
    cont_data_list=0
    
    id_time= endereco_time[time.lower()][-5:]
    end_point_23 = '53241'
    end_point_22 = '44908'
    end_point_21 = '34459'
    
    middle_api=f'/unique-tournament/955/season/'
    
    url_22=base_api + id_time + middle_api + end_point_22 + end_api
    url_23=base_api + id_time + middle_api + end_point_23 + end_api
    url_21=base_api + id_time + middle_api + end_point_21 + end_api
    
    lista_urls=[url_21,url_22]
    
    for url in lista_urls:
        api_link= requests.get(url,headers=browser).json()
        if not 'error' in api_link:
            lista_dados.append(api_link['statistics'])
            if lista_urls.index(lista_urls[cont_url_list])==0:
                lista_dados[cont_data_list]['ano'] =2021
            elif lista_urls.index(lista_urls[cont_url_list])==1:
                  lista_dados[cont_data_list]['ano'] =2022
            elif lista_urls.index(lista_urls[cont_url_list])==2:
                  lista_dados[cont_data_list]['ano'] =2023
            cont_data_list +=1
        cont_url_list +=1
            
    return lista_dados


def construir_dataframe(time:str):
    team = escolhe_time(time)
    
    time_dataframe=pd.DataFrame(index=team[0].keys())
    
    for i in range(len(team)):
        time_dataframe[str(team[i]['ano'])] = team[i].values()
        
    time_dataframe['Media']=time_dataframe.mean(axis=1).apply(lambda x: float('{:.1f}'.format(x)))
    
    return time_dataframe


def construir_grafico(metrica: str, time1:str,time2:str):
    df_time1=construir_dataframe(time1)
    df_time2=construir_dataframe(time2)
    
    anos=[2021,2022]
    
    fig= go.Figure(
        data=[
           go.Bar(name=time1, x=anos,y=[df_time1['2021'][metrica], df_time1['2022'][metrica]]), 
           go.Bar(name=time2, x=anos,y=[df_time2['2021'][metrica], df_time1['2022'][metrica]]) 
        ],
        
        layout_title_text=metrica
    )
    
    return fig.show()
    
    

construir_dataframe('al-hilal')