# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Dados reais sobre a saúde em Pernambuco 
dados_saude_real = pd.DataFrame({
    'Indicador': ['Dengue', 'Tuberculose', 'Mortalidade infantil', 'Acesso a saneamento básico'],
    'Taxa': [120, 15, 8, 44]
})

# Layout do aplicativo
st.title('Saúde em Pernambuco')
st.write('Indicadores de saúde no estado:')

# Gráfico de barras
st.bar_chart(dados_saude_real.set_index('Indicador'))

# Informações contextuais
st.write("""
    - **Dengue**: A dengue é uma doença transmitida pelo mosquito Aedes aegypti. A alta taxa de incidência é preocupante.
    - **Tuberculose**: A tuberculose é uma doença infecciosa que afeta os pulmões. É importante rastrear e tratar casos.
    - **Mortalidade infantil**: A taxa de mortalidade infantil é um indicador crítico da qualidade do sistema de saúde.
    - **Acesso a saneamento básico**: O acesso a água potável e esgoto adequado é fundamental para prevenir doenças.
""")

# Gráficos de barras comparativos
fig_dengue = px.bar(dados_saude_real, x='Indicador', y='Taxa', title='Comparação de Taxa de Dengue')
st.plotly_chart(fig_dengue)

# Análise temporal 
st.write("""
    Tendência ao longo do tempo:
    - A taxa de mortalidade infantil diminuiu 10% nos últimos 5 anos.
    - O acesso a saneamento básico melhorou em áreas urbanas.
""")

# Widgets interativos 
filtro_indicador = st.selectbox('Selecione um indicador:', dados_saude_real['Indicador'])
st.write(f'Você selecionou: {filtro_indicador}')

# Novo widget interativo para resumo sobre doenças
if filtro_indicador == 'Dengue':
    st.write("""
    **Dengue**: A dengue é uma doença viral transmitida pela picada do mosquito Aedes aegypti. Para preveni-la, é importante eliminar água parada, que serve de criadouro para o mosquito, usar repelente e manter o ambiente protegido com telas e mosquiteiros.
    """)
elif filtro_indicador == 'Tuberculose':
    st.write("""
    **Tuberculose**: Causada pela bactéria Mycobacterium tuberculosis, a tuberculose afeta principalmente os pulmões. A prevenção inclui vacinação, boa ventilação dos ambientes e uso de máscaras em locais com aglomeração.
    """)
elif filtro_indicador == 'Mortalidade infantil':
    st.write("""
    **Mortalidade infantil**: A mortalidade infantil é um indicador da qualidade do sistema de saúde e do nível de desenvolvimento social. A redução da taxa de mortalidade infantil pode ser alcançada através de melhorias na assistência pré-natal, no parto e nos cuidados pós-natais, bem como na nutrição e nas condições sanitárias.
    """)
elif filtro_indicador == 'Acesso a saneamento básico':
    st.write("""
    **Acesso a saneamento básico**: O saneamento básico é essencial para a prevenção de diversas doenças, incluindo doenças diarreicas e parasitárias. Investimentos em infraestrutura de saneamento, como esgoto e tratamento de água, são fundamentais para promover a saúde pública e o bem-estar da população.
    """)



