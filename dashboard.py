import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine('postgresql://postgres:postgres@localhost:5432/iot_database')


# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp')
st.plotly_chart(fig1)

# Gráfico 2: Contagem de leituras por hora
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
fig2 = px.line(df_leituras_hora, x='hora', y='contagem')
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'])
st.plotly_chart(fig3)




# Dados de exemplo para inserção
data = {
    'device_id': ['device_1', 'device_2', 'device_1', 'device_3'],
    'temperature': [25.4, 26.1, 24.8, 23.9]
}

# Cria o DataFrame
df = pd.DataFrame(data)

# Insere os dados na tabela 'temperature_readings'
df.to_sql('temperature_readings', engine, if_exists='append', index=False)