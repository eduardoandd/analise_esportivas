import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import webbrowser as wb

df=st.session_state['data']


endereco_time= {'al-hilal':'al-hilal/21895','al-taawoun':'al-taawoun/56021','al-ittihad':'al-ittihad/34315','al-ahli':'/al-ahli/34469','al-ettifaq':'al-ettifaq/34318','al-nassr':'al-nassr/23400','al-fateh':'al-fateh/56023','al-fayha':'al-fayha/168094','al-wehda':'al-wehda/32994','abha':'abha/168090','al-tai':'al-tai/168072','al-khaleej':'al-khaleej/167228','al-akhdood':'al-akhdood/336456','al-raed':'al-raed/56031','al-riyadh':'al-riyadh/168088','damac-fc':'damac-fc/204126','al-shabab':'al-shabab/34313','al-hazem':'al-hazem/168086'}

browser={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

base_api='https://api.sofascore.com/api/v1/team/'
end_api='/statistics/overall'


def escolher_time_2023(time:str):
    data_list= []
    id_time = endereco_time[time.lower()].split('/')[-1]
    session_23='53241'
    middle_api='/unique-tournament/955/season/'
    
    url = base_api + id_time + middle_api + session_23 + end_api
    
    api_link = requests.get(url,headers=browser).json()
    
    if not 'error' in api_link:
        data_list.append(api_link['statistics'])

    
    return data_list

def construir_dataframe_2023(time:str):
    team = escolher_time_2023(time)
    
    time_dataframe=pd.DataFrame(index=team[0].keys())
    time_dataframe['ANO 2023']=team[0].values()
        
    time_dataframe['Media']=time_dataframe.mean(axis=1).apply(lambda x: float('{:.1f}'.format(x)))
    
    return time_dataframe

clubes = endereco_time.keys()
clubes=[clube.capitalize() for clube in clubes]

clube=st.sidebar.selectbox('Clube', clubes)

df=construir_dataframe_2023(clube)
df




