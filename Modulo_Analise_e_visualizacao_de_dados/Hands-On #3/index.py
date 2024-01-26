import streamlit as st
from utils import (
    TITLE,
    APP_TITLE,
)

#Definindo o Título e a Logo do meu projeto
st.set_page_config(
    page_title= TITLE,
    layout="wide",
    initial_sidebar_state="expanded"
    
)

#Título H1
st.title(APP_TITLE)

st.write("Esse dashboard tem como intuito mostrar algumas métricas sobre a agropecuaria e seus impactos ambientais.")

#SideBar
with st.sidebar:
    st.header("Referências")
    st.markdown('🥩 <a hef="https://www.kaggle.com/datasets/selfvivek/environment-impact-of-food-production?select=Food_Production.csv">Environment Impact of Food Production</a>', unsafe_allow_html=True)
    st.markdown('🌐 <a hef="https://ourworldindata.org/">Our World in data</a>', unsafe_allow_html=True)
    

