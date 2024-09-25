import streamlit as st
import plotly.express as px

# Título do dashboard
st.title('Dashboard IoT')

# Carregar dados da view
view_name = 'avg_temp_por_dispositivo'
df_avg_temp = load_data_from_view(view_name)

# Exibir gráfico interativo da média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
fig = px.bar(df_avg_temp, x='device_id', y='avg_temp', title='Média de Temperatura por Dispositivo')
st.plotly_chart(fig)
