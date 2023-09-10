
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
from main import Insights
from lxml import html



endereco_liga = {'arabia':'saudi-arabia/saudi-professional-league/955','inglaterra':'england/premier-league/17'}

endereco_time= {'al-hilal':'al-hilal/21895','al-taawoun':'al-taawoun/56021','al-ittihad':'al-ittihad/34315','al-ahli':'/al-ahli/34469','al-ettifaq':'al-ettifaq/34318','al-nassr':'al-nassr/23400','al-fateh':'al-fateh/56023','al-fayha':'al-fayha/168094','al-wehda':'al-wehda/32994','abha':'abha/168090','al-tai':'al-tai/168072','al-khaleej':'al-khaleej/167228','al-akhdood':'al-akhdood/336456','al-raed':'al-raed/56031','al-riyadh':'al-riyadh/168088','damac-fc':'damac-fc/204126','al-shabab':'al-shabab/34313','al-hazem':'al-hazem/168086'}

endereco_time_inglaterra={'manchester-city':'manchester-city/17','tottenham-hotspur':'tottenham-hotspur/33'}

browser={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

base_api='https://api.sofascore.com/api/v1/team/'
end_api='/statistics/overall'

clubes = endereco_time.keys()
clubes_ing = endereco_time_inglaterra.keys()
#clubes=[clube.capitalize() for clube in clubes]
ligas = ['Inglesa','Saudita']
ligas = st.sidebar.selectbox('Ligas',ligas)

clube=st.sidebar.selectbox('Clube', clubes)
clube_ing=st.sidebar.selectbox('Clube', endereco_time_inglaterra)


insights1 = Insights(clube_ing,2023)
df=insights1.gera_dataframe(liga='inglaterra')
df


    




