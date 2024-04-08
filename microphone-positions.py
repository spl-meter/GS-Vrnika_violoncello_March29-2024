import streamlit as st
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import plotly
plotly.offline.init_notebook_mode()

CSH=px.colors.qualitative.Safe
MS=3

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


def add_point(x,y,z,x0,y0,z0):
    x.append(x0)
    y.append(y0)
    z.append(z0)

    return x,y,z


df_mic=pd.read_excel(open('koordinate.xlsx', 'rb'),sheet_name='mikrofoni')
df_mic.columns=['signal','x','y','z']
df_mic.index=df_mic.index+1
for kk in range(42):
    df_mic.signal.iloc[kk]='signal '+str(kk+1)

#df_mic = df_mic.drop('#', axis=1)

df_izvori=pd.read_excel(open('koordinate.xlsx', 'rb'),sheet_name='izvori')
df_izvori.columns=['lega','x','y','z']

df_vogali=pd.read_excel(open('koordinate.xlsx', 'rb'),sheet_name='vogali')
df_vogali.columns=['vogal','x','y','z']


df_mic.x=-df_mic.x
df_izvori.x=-df_izvori.x
df_vogali.x=-df_vogali.x

st.markdown('##  Microphone coordinates')

st.markdown(' ')
st.markdown('Recording session: March 29, 2024, GŠ Vrnika')

st.markdown('The coordinates of the microphones and violoncello during the recordings are providedused.')

col1, col2 = st.columns(2) 
col1.markdown('### Microphone coordinates')
col1.dataframe(df_mic)

col2.markdown('### Violoncello coordinates')
col2.dataframe(df_izvori)


trace1 = go.Scatter3d(
    x=df_mic.x,
    y=df_mic.y,
    z=df_mic.z,
    text=df_mic.signal,
    mode='markers',
    name='microphones',
    marker_size=2,
    
)

trace1B = go.Scatter3d(
    x=df_izvori.x,
    y=df_izvori.y,
    z=df_izvori.z,
    text=df_izvori.lega,
    mode='markers',
    name='violoncello',
    marker_size=5,
    
)

x_lines = list()
y_lines = list()
z_lines = list()

kk=0
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=1
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=2
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=3
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=0
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=4
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=5
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=6
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=7
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=4
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=5
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=1
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=2
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=6
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=7
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])
kk=3
[x_lines,y_lines,z_lines]=add_point(x_lines,y_lines,z_lines,df_vogali.x.iloc[kk],df_vogali.y.iloc[kk],df_vogali.z.iloc[kk])



x1 = list();y1 = list();z1 = list(); 

for kk in range(0,6):
    x1.append(df_mic.x.iloc[kk])
    y1.append(df_mic.y.iloc[kk])
    z1.append(df_mic.z.iloc[kk])
tr_m1 = go.Scatter3d(x=x1,y=y1,z=z1,mode='lines', name='mics line 1')

x1 = list();y1 = list();z1 = list(); 
for kk in range(6,12):
    x1.append(df_mic.x.iloc[kk])
    y1.append(df_mic.y.iloc[kk])
    z1.append(df_mic.z.iloc[kk])
tr_m2 = go.Scatter3d(x=x1,y=y1,z=z1,mode='lines', name='mics line 2')

x1 = list();y1 = list();z1 = list(); 
for kk in range(12,18):
    x1.append(df_mic.x.iloc[kk])
    y1.append(df_mic.y.iloc[kk])
    z1.append(df_mic.z.iloc[kk])
tr_m3 = go.Scatter3d(x=x1,y=y1,z=z1,mode='lines', name='mics line 3')

x1 = list();y1 = list();z1 = list();
for kk in range(18,24):
    x1.append(df_mic.x.iloc[kk])
    y1.append(df_mic.y.iloc[kk])
    z1.append(df_mic.z.iloc[kk])
tr_m4 = go.Scatter3d(x=x1,y=y1,z=z1,mode='lines', name='mics line 4')

x1 = list();y1 = list();z1 = list(); 
for kk in range(24,30):
    x1.append(df_mic.x.iloc[kk])
    y1.append(df_mic.y.iloc[kk])
    z1.append(df_mic.z.iloc[kk])
tr_m5 = go.Scatter3d(x=x1,y=y1,z=z1,mode='lines', name='mics line 5')

x1 = list();y1 = list();z1 = list(); 
for kk in range(30,36):
    x1.append(df_mic.x.iloc[kk])
    y1.append(df_mic.y.iloc[kk])
    z1.append(df_mic.z.iloc[kk])
tr_m6 = go.Scatter3d(x=x1,y=y1,z=z1,mode='lines', name='mics line 6')

x1 = list();y1 = list();z1 = list(); 
for kk in range(36,42):
    x1.append(df_mic.x.iloc[kk])
    y1.append(df_mic.y.iloc[kk])
    z1.append(df_mic.z.iloc[kk])
tr_m7 = go.Scatter3d(x=x1,y=y1,z=z1,mode='lines', name='mics line 7')

trace2 = go.Scatter3d(
    x=x_lines,
    y=y_lines,
    z=z_lines,
    mode='lines',
    name='room corners'
)

fig = go.Figure(data=[trace1, trace1B, trace2,tr_m1,tr_m2,tr_m3,tr_m4,tr_m5,tr_m6,tr_m7])
st.plotly_chart(fig, filename='room',use_container_width=True,height=1800)

