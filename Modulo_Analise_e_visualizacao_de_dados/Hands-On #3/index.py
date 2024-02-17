import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import folium

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
        options=["Sobre", "Países"],
        icons=['globe', 'map','database'],
        menu_icon='globe',
        default_index=0,
        orientation='horizontal',
)

#Lendo arquivo csv
df = pd.read_csv("assets/data/global_education_sep.csv")

#Pagina para cada opção selecionada
#Página sobre para explicar sobre o projeto
if selecionar == "Sobre":
        st.title(f"Você Selecionou {selecionar}")
        st.title("Dados Educacionais Mundiais")
        st.write("""Explorando Dados Educacionais Globais com Streamlit

Este projeto oferece uma análise interativa e visualmente atraente dos dados educacionais globais. Os usuários podem escolher entre diferentes opções de menu para explorar informações sobre países, além de outras análises específicas.

**Recursos Principais:**

- **Página Sobre:** Fornece uma visão geral do projeto e sua importância.
- **Página Países:** Permite aos usuários visualizar gráficos sobre taxas de abandono e conclusão escolar em países específicos, além de um mapa de calor interativo para diferentes indicadores educacionais.

**Funcionalidades:**

- **Seleção de Países e Métricas:** Os usuários podem selecionar um país específico e uma métrica de interesse para visualizar gráficos detalhados.
- **Mapa de Calor Interativo:** Um mapa de calor interativo é gerado com base na métrica selecionada, permitindo a visualização das tendências geográficas.
- **Personalização Visual:** Os gráficos e o layout foram projetados para oferecer uma experiência de usuário agradável e informativa.

Para mais detalhes sobre o conjunto de dados original, acesse [aqui](https://www.kaggle.com/datasets/nelgiriyewithana/world-educational-data).
""")

#Página Países fornece gráficos para alguns dados de taxas de escolaridade em países ao redor do mundo
# Página Países fornece gráficos para alguns dados de taxas de escolaridade em países ao redor do mundo
if selecionar == "Países":
    st.title(f"Você Selecionou {selecionar}")

    col1, col2 = st.columns(2)
    # pegando o pais selecionado
    # Definindo colunas para metricas
    with col1: 
        st.title("Gráfico de Taxa de Abandono/Conclusão por País:")
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
        
       
    with col2:
          st.text("Este gráfico de barras interativo exibe a taxa de abandono ou conclusão\nescolar em diferentes estágios da educação para o país selecionado. \nOs usuários podem escolher o país de interesse e a métrica desejada (abandono ou conclusão)\n, proporcionando uma visão detalhada das tendências educacionais em cada país.")
    
        
    # Subtítulo
    st.title("Mapa de Calor Geográfico:")

    # Filtrar os dados para obter apenas as informações necessárias
    data_filtered = df[['Países e regiões', 'Latitude', 'Longitude',
        'Taxa de abandono pré-primário (idade masculina)',
        'Taxa de abandono pré-primário (idade feminina)',
        'Taxa de abandono no ensino primário (idade masculina)',
        'Taxa de abandono no ensino primário (idade feminina)',
        'Taxa de abandono no ensino fundamental inferior (idade masculina)',
        'Taxa de abandono no ensino fundamental inferior (idade feminina)',
        'Taxa de abandono no ensino fundamental superior (idade masculina)',
        'Taxa de abandono no ensino fundamental superior (idade feminina)',
        'Taxa de conclusão no ensino primário (idade masculina)',
        'Taxa de conclusão no ensino primário (idade feminina)',
        'Taxa de conclusão no ensino fundamental inferior (idade masculina)',
        'Taxa de conclusão no ensino fundamental inferior (idade feminina)',
        'Taxa de conclusão no ensino fundamental superior (idade masculina)',
        'Taxa de conclusão no ensino fundamental superior (idade feminina)',
        'Taxa de alfabetização para jovens de 15 a 24 anos (sexo masculino)',
        'Taxa de alfabetização para jovens de 15 a 24 anos (sexo feminino)',
        'Taxa de desemprego']].dropna()

    # Calcular médias para diferentes indicadores
    data_filtered['Taxa Média de Abandono'] = data_filtered[[col for col in data_filtered.columns if 'Taxa de abandono' in col]].mean(axis=1)
    data_filtered['Taxa Média de Conclusão'] = data_filtered[[col for col in data_filtered.columns if 'Taxa de conclusão' in col]].mean(axis=1)
    data_filtered['Taxa Média de Alfabetização'] = data_filtered[['Taxa de alfabetização para jovens de 15 a 24 anos (sexo masculino)',
                                                                'Taxa de alfabetização para jovens de 15 a 24 anos (sexo feminino)']].mean(axis=1)
    data_filtered['Taxa de Desemprego'] = data_filtered['Taxa de desemprego']

    data_medias = data_filtered[['Taxa Média de Abandono', 'Taxa Média de Conclusão', 'Taxa Média de Alfabetização', 'Taxa de Desemprego']]

    media_select = st.selectbox("Selecione a Taxa desejada: ", data_medias.columns)

    # Criar um mapa de calor interativo usando Plotly
    fig = px.density_mapbox(data_filtered, lat='Latitude', lon='Longitude', z=data_medias[media_select],
                            radius=10, center=dict(lat=0, lon=0), zoom=1,
                            mapbox_style="carto-positron", title=f"Mapa de Calor da {media_select}",
                            hover_name='Países e regiões', opacity=0.7)
    fig.update_layout(margin=dict(b=0, t=0, l=0, r=0), width =1024, height=720)
    fig.update_coloraxes(colorbar_title=f"{media_select}")

    # Exibir o mapa de calor no dashboard
    st.plotly_chart(fig)
        






    
    


