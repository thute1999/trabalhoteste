import streamlit as st
import pandas as pd
import numpy as np

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide"
)

# TÍTULO
st.title("📊 Dashboard de Vendas")
st.markdown("Exemplo simples com dados fictícios")

# DADOS FICTÍCIOS
np.random.seed(42)

meses = [
    "Jan", "Fev", "Mar", "Abr",
    "Mai", "Jun", "Jul", "Ago",
    "Set", "Out", "Nov", "Dez"
]

vendas = np.random.randint(1000, 5000, 12)
clientes = np.random.randint(50, 300, 12)
lucro = np.random.randint(500, 2500, 12)

df = pd.DataFrame({
    "Mês": meses,
    "Vendas": vendas,
    "Clientes": clientes,
    "Lucro": lucro
})

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "💰 Total de Vendas",
    f"R$ {df['Vendas'].sum():,.0f}"
)

col2.metric(
    "👥 Total de Clientes",
    f"{df['Clientes'].sum()}"
)

col3.metric(
    "📈 Lucro Total",
    f"R$ {df['Lucro'].sum():,.0f}"
)

st.divider()

# GRÁFICOS
col4, col5 = st.columns(2)

with col4:
    st.subheader("Vendas por Mês")
    st.bar_chart(df.set_index("Mês")["Vendas"])

with col5:
    st.subheader("Lucro por Mês")
    st.line_chart(df.set_index("Mês")["Lucro"])

# TABELA
st.subheader("📋 Dados")
st.dataframe(df, use_container_width=True)

# RODAPÉ
st.markdown("---")
st.caption("Dashboard criado com Streamlit")