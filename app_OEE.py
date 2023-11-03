#from codigo_de_ejecucion import *
import json
import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector as mariadb
import streamlit as st
from streamlit_echarts import st_echarts
import datetime
import pymysql
import plotly.graph_objects as go

#Automcompletar rápido

#CONFIGURACION DE LA PÁGINA
st.set_page_config(
	page_title = 'Enplast  KPIs Program Data',
	page_icon = 'LogoEnplast.png',
	layout = 'wide')

#SIDEBAR
with st.sidebar:
	st.image('ImagenEmpresa.png')

    #INPUTS DE LA APLICACION
	fecha = st.date_input('Seleccione fecha:', datetime.date(2023, 1, 1))
	st.write('la Fecha seleccionada es:', fecha)

#MAIN
st.title('ENPLAST Calculo del OEE')


#CALCULAR

#fecha="2023-10-22"
# Crear la conexión MySQL
try:
	con = create_engine(f'mysql+mysqlconnector://Jorge:j0rg3!@10.0.0.77/Enplast')
except pymysql.err.OperationalError:
	print("Error conectando con la base de datos.")

# Leer los datos de una tabla en MySQL y almacenarlos en un objeto de Pandas DataFrame
#df = pd.read_sql(sql="select oee from calculo_oee_diario where maquina=1 and fecha='%s'"%fecha, con=con)
#df = pd.read_sql(sql="select * from calculo_oee_diario where maquina=1", con=con)


Maquina_1=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=1 and fecha='%s'"%fecha, con=con)
Maquina_2=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=2 and fecha='%s'"%fecha, con=con)
Maquina_5=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=5 and fecha='%s'"%fecha, con=con)
Maquina_6=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=6 and fecha='%s'"%fecha, con=con)
Maquina_9=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=9 and fecha='%s'"%fecha, con=con)
Maquina_10=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=10 and fecha='%s'"%fecha, con=con)
Maquina_11=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=11 and fecha='%s'"%fecha, con=con)
Maquina_12=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=12 and fecha='%s'"%fecha, con=con)
Maquina_13=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=13 and fecha='%s'"%fecha, con=con)
Maquina_14=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=14 and fecha='%s'"%fecha, con=con)
Maquina_16=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=16 and fecha='%s'"%fecha, con=con)
Maquina_17=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=17 and fecha='%s'"%fecha, con=con)
Maquina_72=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=72 and fecha='%s'"%fecha, con=con)
Maquina_73=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=73 and fecha='%s'"%fecha, con=con)
Maquina_74=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=74 and fecha='%s'"%fecha, con=con)
Maquina_75=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=75 and fecha='%s'"%fecha, con=con)
Maquina_76=pd.read_sql(sql="select oee from calculo_oee_diario where maquina=76 and fecha='%s'"%fecha, con=con)



#CALCULAR RIESGO

    
    #Calcular los kpis  

    #Velocimetros
    #Velocimetro para Maquina1
	
    #Representarlos en la app
if st.sidebar.button('OBTENER OEE'):

	col1, col2,col3, col4, col5, col6 = st.columns(6)
	with col1:		
		Lista1=Maquina_1.to_numpy().tolist()
		Valor1=Lista1[0]
		option1 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor1,
					"name": 'Maquina 1'}]
			}]
		};
		st_echarts(options=option1,width="100%", key="0")

	with col2:
		Lista2=Maquina_2.to_numpy().tolist()
		Valor2=Lista2[0]
		option2 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor2,
					"name": 'Maquina 2'}]
			}]
		};
		st_echarts(options=option2,width="100%", key="1")
		
	with col3:
		Lista5=Maquina_5.to_numpy().tolist()
		Valor5=Lista5[0]
		option5 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor5,
					"name": 'Maquina 5'}]
			}]
		};
		st_echarts(options=option5,width="100%", key="3")
			

	with col4:
		Lista6=Maquina_6.to_numpy().tolist()
		Valor6=Lista6[0]
		option6 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor6,
					"name": 'Maquina 6'}]
			}]
		};
		st_echarts(options=option6,width="100%", key="4")
			
	with col5:
		Lista9=Maquina_9.to_numpy().tolist()
		Valor9=Lista9[0]
		option9 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor9,
					"name": 'Maquina 5'}]
			}]
		};
		st_echarts(options=option9,width="100%", key="5")
		
		
	with col6:
		Lista10=Maquina_10.to_numpy().tolist()
		Valor10=Lista10[0]
		option10 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor10,
					"name": 'Maquina 10'}]
			}]
		};
		st_echarts(options=option10,width="100%", key="6")
	
	#Fila 2
	col1, col2,col3, col4, col5, col6 = st.columns(6)
	with col1:
		Lista11=Maquina_11.to_numpy().tolist()
		Valor11=Lista11[0]
		option11 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor11,
					"name": 'Maquina 11'}]
			}]
		};
		st_echarts(options=option11,width="100%", key="7")
	with col2:
		Lista12=Maquina_12.to_numpy().tolist()
		Valor12=Lista12[0]
		option12 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor12,
					"name": 'Maquina 12'}]
			}]
		};
		st_echarts(options=option12,width="100%", key="8")
	with col3:
		Lista13=Maquina_13.to_numpy().tolist()
		Valor13=Lista13[0]
		option13 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor13,
					"name": 'Maquina 13'}]
			}]
		};
		st_echarts(options=option13,width="100%", key="9")
	with col4:
		Lista14=Maquina_14.to_numpy().tolist()
		Valor14=Lista14[0]
		option14 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor14,
					"name": 'Maquina 14'}]
			}]
		};
		st_echarts(options=option14,width="100%", key="10")
	with col5:
		Lista16=Maquina_16.to_numpy().tolist()
		Valor16=Lista16[0]
		option16 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor16,
					"name": 'Maquina 16'}]
			}]
		};
		st_echarts(options=option16,width="100%", key="11")
	with col6:
		Lista17=Maquina_17.to_numpy().tolist()
		Valor17=Lista17[0]
		option17 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor17,
					"name": 'Maquina 17'}]
			}]
		};
		st_echarts(options=option17,width="100%", key="12")
		
	#Fila 3
	col1, col2,col3, col4, col5 = st.columns(5)
	with col1:
		Lista72=Maquina_72.to_numpy().tolist()
		Valor72=Lista72[0]
		option72 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor72,
					"name": 'Maquina 72'}]
			}]
		};
		st_echarts(options=option72,width="100%", key="13")
	with col2:
		Lista73=Maquina_73.to_numpy().tolist()
		Valor73=Lista73[0]
		option73 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor73,
					"name": 'Maquina 73'}]
			}]
		};
		st_echarts(options=option73,width="100%", key="14")
	with col3:
		Lista74=Maquina_74.to_numpy().tolist()
		Valor74=Lista74[0]
		option74 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor74,
					"name": 'Maquina 74'}]
			}]
		};
		st_echarts(options=option74,width="100%", key="15")
	with col4:
		Lista75=Maquina_75.to_numpy().tolist()
		Valor75=Lista75[0]
		option75 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'
			},
			"series": [{
				"name": 'YYY',
				"type": 'gauge',
				"startAngle": 220,
				"endAngle": -50,
				"progress": {"show": "true"},
				"radius":'100%',
				"itemStyle": {
					"color": '#1580E0', #58D9F9,
					"shadowColor": 'rgba(0,0,0,0)',
					"shadowBlur": 10,
					"shadowOffsetX": 2,
					"shadowOffsetY": 2,
					"radius": '55%',},
				"progress": {
					"show": "true",
					"roundCap": "true",
					"width": 5},
				"pointer": {
					"length": '60%',
					"width": 8,
					"offsetCenter": [0, '5%']},
				"detail": {
					"valueAnimation": "true",
					"formatter": '{value}%',
					"backgroundColor": '#000000',
					"borderColor": '#000000',
					"borderWidth": 5,
					"width": '0%',
					"lineHeight": 10,
					"height": 10,
					"borderRadius": 188,
					"offsetCenter": [0, '100%'],
					"valueAnimation": "true",},
				"data": [{
					"value": Valor75,
					"name": 'Maquina 75'}]
			}]
		};
		st_echarts(options=option75,width="100%", key="16")
	with col5:
		Lista76=Maquina_76.to_numpy().tolist()
		Valor76=Lista76[0]
		option76 = {
			"tooltip": {
			"formatter": '{a} <br/>{b} : {c}%'},
			"series": [
				{"name": 'Current',
				"type": 'gauge',
				"progress": {
				"show": False},
				"axisLine": {
				"lineStyle": {
				"width": 6,
				"color": [
					[0.2, 'rgb(235, 34, 14)'],
					[0.4, 'rgb(242, 99, 9)'],
					[0.6, 'rgb(250, 197, 21)'],
					[0.8, 'rgb(117, 198, 5)'],
					[1, 'rgb(56, 182, 14)']
					]}
			},
			"detail": {
				"valueAnimation": True,
				"formatter":'{value}%',
				"color": 'auto'
			},
			"data": [
			{
				"value": Valor76,
				"name": 'Maquina 76'
			},
			]
		}
		]
		};
		st_echarts(options=option76,width="100%", key="17")
	
else:
	st.write('Selecciona una fecha Correctamente')
