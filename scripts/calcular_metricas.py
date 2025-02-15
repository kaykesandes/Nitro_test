import pandas as pd
import App.scripts.load_data as load_data

loja1, loja2, loja3, lojas, produtos, df = load_data.load_data()

# Funções para calcular métricas
def calcular_total_faturado(loja1, loja2, loja3):
    # Calcular o total faturado por loja
    total_faturado_loja1 = loja1["ValorVenda"].sum()
    total_faturado_loja2 = loja2["ValorVenda"].sum()
    total_faturado_loja3 = loja3["ValorVenda"].sum()
    
    return total_faturado_loja1, total_faturado_loja2, total_faturado_loja3

def calcular_top_vendedores(loja1, loja2, loja3):
    # Calcular o top vendedores por loja
    vendendor_loja1 = loja1.groupby("Nome Vendedor")["ValorVenda"].sum().reset_index().sort_values(by="ValorVenda", ascending=False)
    vendendor_loja2 = loja2.groupby("Nome Vendedor")["ValorVenda"].sum().reset_index().sort_values(by="ValorVenda", ascending=False)
    vendendor_loja3 = loja3.groupby("Nome Vendedor")["ValorVenda"].sum().reset_index().sort_values(by="ValorVenda", ascending=False)

    return vendendor_loja1, vendendor_loja2, vendendor_loja3