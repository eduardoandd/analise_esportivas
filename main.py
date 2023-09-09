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




#NECESSÁRIO PENSAR EM UM JEITO DE FAZER OS GRÁFICOS.....



endereco_time= {'al-hilal':'al-hilal/21895','al-taawoun':'al-taawoun/56021','al-ittihad':'al-ittihad/34315','al-ahli':'/al-ahli/34469','al-ettifaq':'al-ettifaq/34318','al-nassr':'al-nassr/23400','al-fateh':'al-fateh/56023','al-fayha':'al-fayha/168094','al-wehda':'al-wehda/32994','abha':'abha/168090','al-tai':'al-tai/168072','al-khaleej':'al-khaleej/167228','al-akhdood':'al-akhdood/336456','al-raed':'al-raed/56031','al-riyadh':'al-riyadh/168088','damac-fc':'damac-fc/204126','al-shabab':'al-shabab/34313','al-hazem':'al-hazem/168086'}
    



browser={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

base_api='https://api.sofascore.com/api/v1/team/'
end_api='/statistics/overall'   

class Insights:
    def __init__(self,time,ano):
        self.time=time
        self.ano = ano
        
        
    def escolhe_time(self):
        
        if self.ano < 2023:
            
            data_list = []
            cont_url_list =0
            cont_data_list=0
            
            id_time = endereco_time[self.time].split('/')[-1]
            session_21 = '34459'
            session_22 = '44908'
            
            middle_api=f'/unique-tournament/955/season/'
            url_21=base_api + id_time + middle_api + session_21 + end_api
            url_22=base_api + id_time + middle_api + session_22 + end_api
            url_list = [url_21,url_22]
            
            for url in url_list:
                api_link= requests.get(url,headers=browser).json()
                if not 'error' in api_link:
                    data_list.append(api_link['statistics'])
                    if url_list.index(url_list[cont_url_list])==0:
                        data_list[cont_data_list]['ano'] =2021
                    elif url_list.index(url_list[cont_url_list])==1:
                        data_list[cont_data_list]['ano'] = 2022
                    cont_data_list +=1
                cont_url_list +=1
             
        else:
            data_list= []
            id_time = endereco_time[self.time].split('/')[-1]
            session_23='53241'
            middle_api='/unique-tournament/955/season/'
    
            url = base_api + id_time + middle_api + session_23 + end_api
    
            api_link = requests.get(url,headers=browser).json()
    
            if not 'error' in api_link:
                data_list.append(api_link['statistics'])

        return data_list

    def gera_dataframe(self):
        team = self.escolhe_time()
        team_dataframe = pd.DataFrame(index=team[0].keys())
        
        if self.ano < 2023:
            for i in range(len(team)):
                team_dataframe[str(team[i]['ano'])] = team[i].values()
        else:
            team_dataframe['Media']=team_dataframe.mean(axis=1).apply(lambda x: float('{:.1f}'.format(x)))
            
        team_dataframe.mean(axis=1).apply(lambda x: float('{:.1f}'.format(x)))
        
        return team_dataframe


# i =Insights('al-hilal',2023)
# i.gera_dataframe()










# def construir_grafico(metrica: str, time1:str,time2:str):
#     df_time1=construir_dataframe(time1)
#     df_time2=construir_dataframe(time2)
    
#     anos=[2021,2022]
    
#     fig= go.Figure(
#         data=[
#            go.Bar(name=time1, x=anos,y=[df_time1['2021'][metrica], df_time1['2022'][metrica]]), 
#            go.Bar(name=time2, x=anos,y=[df_time2['2021'][metrica], df_time1['2022'][metrica]]) 
#         ],
        
#         layout_title_text=metrica
#     )
    
#     return fig.show()


    