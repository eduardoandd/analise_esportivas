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
            
            id_time = endereco_time[self.time.lower()].split('/')[-1]
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
                
            return data_list
        
        else:
            data_list= []
            id_time = endereco_time[self.time.lower()].split('/')[-1]
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
        
            
            
        
    


insights1 = Insights('al-hilal',2023)
insights1.gera_dataframe()




def construir_dataframe(time:str):
    team = escolhe_time(time)
    
    time_dataframe=pd.DataFrame(index=team[0].keys())
    
    for i in range(len(team)):
        time_dataframe[str(team[i]['ano'])] = team[i].values()
        
    time_dataframe['Media']=time_dataframe.mean(axis=1).apply(lambda x: float('{:.1f}'.format(x)))
    
    return time_dataframe



# def escolhe_time(time:str):
#     lista_dados=  []
#     cont_url_list=0
#     cont_data_list=0
    
#     id_time = endereco_time[time.lower()].split('/')[-1]
#     end_point_23 = '53241'
#     end_point_22 = '44908'
#     end_point_21 = '34459'
    
#     middle_api=f'/unique-tournament/955/season/'
    
#     url_22=base_api + id_time + middle_api + end_point_22 + end_api
#     url_23=base_api + id_time + middle_api + end_point_23 + end_api
#     url_21=base_api + id_time + middle_api + end_point_21 + end_api
    
#     lista_urls=[url_21,url_22]
    
    
    
    # for url in lista_urls:
    #     api_link= requests.get(url,headers=browser).json()
    #     if not 'error' in api_link:
    #         lista_dados.append(api_link['statistics'])
    #         if lista_urls.index(lista_urls[cont_url_list])==0:
    #             lista_dados[cont_data_list]['ano'] =2021
    #         elif lista_urls.index(lista_urls[cont_url_list])==1:
    #               lista_dados[cont_data_list]['ano'] =2022
    #         elif lista_urls.index(lista_urls[cont_url_list])==2:
    #               lista_dados[cont_data_list]['ano'] =2023
    #         cont_data_list +=1
    #     cont_url_list +=1
            
    # return lista_dados




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


    

#construir_dataframe_2023('al-riyadh')


df=construir_dataframe_2023('al-hilal')


if 'data' not in st.session_state:
    st.session_state['data'] = df
    
st.markdown('# ANÁLISE ESPORTIVAS')
st.sidebar.markdown('Desenvolvido por [mim](https://github.com/eduardoandd)')

btn=st.button('Dados retirados do [SofasCore](https://www.sofascore.com/)')

if btn:
    wb.open_new_tab('https://www.sofascore.com/')
    