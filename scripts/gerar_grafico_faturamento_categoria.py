import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from scripts.load_data import load_data


import os
os.makedirs('App/solucao', exist_ok=True)


matplotlib.use('Agg')

def gerar_grafico_faturamento_categoria(df):
    # Gráfico de faturamento mensal
    plt.figure(figsize=(10, 5))
    sns.barplot(x=df["Mes"].astype(str), y=df["ValorVenda"], hue=df["Cidade"], palette="viridis")
    plt.xlabel("Mês")
    plt.ylabel("Faturamento (R$)")
    plt.title("Faturamento Mensal por Loja")
    plt.legend(title="Loja")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig("static/faturamento_mensal.png")
    plt.savefig("solucao/faturamento_mensal.png")
    plt.close()

    # Gráfico de faturamento por categoria
    plt.figure(figsize=(10, 5))
    sns.barplot(x=df["Categoria"], y=df["ValorVenda"], hue=df["Cidade"], palette="coolwarm")
    plt.xlabel("Categoria")
    plt.ylabel("Faturamento (R$)")
    plt.title("Faturamento por Categoria de Produto")
    plt.legend(title="Loja")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig("static/faturamento_categoria.png")
    plt.savefig("solucao/faturamento_categoria.png")
    plt.close()

# Carregar dados usando a função load_data
loja1, loja2, loja3, lojas, produtos, df = load_data()

# Gerar gráficos
gerar_grafico_faturamento_categoria(df)