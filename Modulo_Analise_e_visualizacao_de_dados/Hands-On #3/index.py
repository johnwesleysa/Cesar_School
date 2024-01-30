import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

#Definindo o Título
st.set_page_config(
    page_title= 'Titulo',
    layout="wide",
    initial_sidebar_state="expanded"
    
)

#chamando a leitura da custom css
with open('assets/style/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Container para logo
with st.container():
    st.image('assets/img/logo.png', width=100, )
    st.text('World Education')

#Menu de opções
selecionar = option_menu(
        menu_title="",
        options=["Sobre", "Países", "Outros dados"],
        icons=['globe', 'map','database'],
        menu_icon='globe',
        default_index=0,
        orientation='horizontal',
)

#Lendo arquivo csv
df = pd.read_csv("assets/data/global_education.csv")

#Pagina para cada opção selecionada
#Página sobre para explicar sobre o projeto
if selecionar == "Sobre":
        st.title(f"You have selected {selecionar}")
        st.title("Título Aqui")
        st.write("Breve descrição")

#Página Países fornece gráficos para alguns dados de taxas de escolaridade em países ao redor do mundo
# Página Países fornece gráficos para alguns dados de taxas de escolaridade em países ao redor do mundo
if selecionar == "Países":
    st.title(f"You have selected {selecionar}")

    col1, col2 = st.columns(2)
    # pegando o pais selecionado
    with col1:
        # Definindo colunas para metricas
        lista_metrica = ["Taxa de abandono", "Taxa de conclusão"]
        tx_abandono = [
            'Taxa de abandono pré-primário (idade masculina)',
            'Taxa de abandono pré-primário (idade feminina)',
            'Taxa de abandono no ensino primário (idade masculina)',
            'Taxa de abandono no ensino primário (idade feminina)',
            'Taxa de abandono no ensino fundamental inferior (idade masculina)',
            'Taxa de abandono no ensino fundamental inferior (idade feminina)',
            'Taxa de abandono no ensino fundamental superior (idade masculina)',
            'Taxa de abandono no ensino fundamental superior (idade feminina)',
        ]
        tx_conclusao = [
            'Taxa de conclusão no ensino primário (idade masculina)',
            'Taxa de conclusão no ensino primário (idade feminina)',
            'Taxa de conclusão no ensino fundamental inferior (idade masculina)',
            'Taxa de conclusão no ensino fundamental inferior (idade feminina)',
            'Taxa de conclusão no ensino fundamental superior (idade masculina)',
            'Taxa de conclusão no ensino fundamental superior (idade feminina)',
        ]

        pais_selecionado = st.selectbox("Escolha o país: ", df['Países e regiões'])
        metrica_selecionada = st.selectbox("Selecione a métrica para análise: ", lista_metrica)

        if metrica_selecionada == "Taxa de abandono":
            df_pais = df[df['Países e regiões'] == pais_selecionado]

            # Obtenha os valores ordenados em ordem decrescente
            valores_ordenados = df_pais[tx_abandono].values[0]
            valores_ordenados = pd.Series(valores_ordenados, index=tx_abandono)
            valores_ordenados = valores_ordenados.sort_values(ascending=True)

            # Crie o gráfico com Plotly Express
            fig = px.bar(x=valores_ordenados.values, y=valores_ordenados.index, orientation='h')
            fig.update_layout(title=f'Taxa de Abandono em {pais_selecionado}',
                              xaxis_title='Taxa de Abandono',
                              yaxis_title='Ano ou Categoria')

            st.plotly_chart(fig)

        elif metrica_selecionada == "Taxa de conclusão":
            df_pais = df[df['Países e regiões'] == pais_selecionado]

            # Obtenha os valores ordenados em ordem decrescente
            valores_ordenados = df_pais[tx_conclusao].values[0]
            valores_ordenados = pd.Series(valores_ordenados, index=tx_conclusao)
            valores_ordenados = valores_ordenados.sort_values(ascending=False)

            # Crie o gráfico com Plotly Express
            fig = px.bar(x=valores_ordenados.values, y=valores_ordenados.index, orientation='h')
            fig.update_layout(title=f'Taxa de Conclusão em {pais_selecionado}',
                              xaxis_title='Taxa de Conclusão',
                              yaxis_title='Ano ou Categoria')

            st.plotly_chart(fig)

#Página Outros dados para outras informações presentes no dataset
if selecionar == "Outros dados":
        st.title(f"You have selected {selecionar}")






    
    

