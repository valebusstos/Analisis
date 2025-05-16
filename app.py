import pandas as pd 
import streamlit as st 
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as  plt 

st.title('Análisis')

df = pd.read_csv('datos_man1.csv')

tab1, tab2 = st.tabs(['Tab1', 'Tab2'])

with tab1:

    tabfreq1 = df['Estacion'].value_counts().sort_index()
    tabfreq2 = df['Hora'].value_counts().sort_index()
    tabfreq3 = df['Pasajeros'].value_counts().sort_index()
    tabfreq4 = df['Tiempo_espera_min'].value_counts().sort_index()
    tabfreq5 = df['Puntual'].value_counts().sort_index()
    tabfreq6 = df['Clima'].value_counts().sort_index()

    fig1 = px.bar(tabfreq1, y = 'count')
    fig2 = px.bar(tabfreq2, y = 'count')
    fig3 = px.histogram(df, x = 'Pasajeros')
    fig4 = px.histogram(df, x = 'Tiempo_espera_min')
    fig5 = px.bar(tabfreq5, y = 'count')
    fig6 = px.bar(tabfreq6, y = 'count')

    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)

with tab2:
    fig, ax = plt.subplots(2,3, figsize=(10,4))
    
    ax[0,0].scatter(df['Estacion'], df['Tiempo_espera_min'])
    ax[0,1].scatter(df['Hora'], df['Tiempo_espera_min'])
    ax[0,2].scatter(df['Pasajeros'], df['Tiempo_espera_min'])
    ax[1,0].scatter(df['Puntual'], df['Tiempo_espera_min'])
    ax[1,1].scatter(df['Clima'], df['Tiempo_espera_min'])

    st.pyplot(fig)

    