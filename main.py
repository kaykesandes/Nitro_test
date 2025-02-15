from flask import Flask, render_template
import pandas as pd
from App.scripts.load_data import load_data
from App.scripts.calcular_metricas import calcular_total_faturado, calcular_top_vendedores
from App.scripts.gerar_grafico_faturamento_categoria import gerar_grafico_faturamento_categoria
from App.powerbi.generate_powerbi_report import generate_powerbi_report 

app = Flask(__name__)

try:
    loja1, loja2, loja3, lojas, produtos, df = load_data()
    total_faturado = df["ValorVenda"].sum()
    total_faturado_loja1, total_faturado_loja2, total_faturado_loja3 = calcular_total_faturado(loja1, loja2, loja3)
    top_vendedores_loja1, top_vendedores_loja2, top_vendedores_loja3 = calcular_top_vendedores(loja1, loja2, loja3)
    soma_total_faturado = total_faturado_loja1 + total_faturado_loja2 + total_faturado_loja3
    
    gerar_grafico_faturamento_categoria(df)
    
    generate_powerbi_report(df, total_faturado, total_faturado_loja1, total_faturado_loja2, total_faturado_loja3, top_vendedores_loja1, top_vendedores_loja2, top_vendedores_loja3, soma_total_faturado)
except Exception as e:
    print(f"Erro ao carregar ou processar os dados: {e}")
    df = pd.DataFrame()
    total_faturado = 0
    total_faturado_loja1 = 0
    total_faturado_loja2 = 0
    total_faturado_loja3 = 0
    top_vendedores_loja1 = pd.DataFrame()
    top_vendedores_loja2 = pd.DataFrame()
    top_vendedores_loja3 = pd.DataFrame()
    soma_total_faturado = 0

@app.route('/')
def index():
    return render_template('index.html', data=df, total_faturado=total_faturado, 
                           total_faturado_loja1=total_faturado_loja1, total_faturado_loja2=total_faturado_loja2, 
                           total_faturado_loja3=total_faturado_loja3, soma_total_faturado=soma_total_faturado,
                           top_vendedor_loja1=top_vendedores_loja1, top_vendedor_loja2=top_vendedores_loja2, top_vendedor_loja3=top_vendedores_loja3,)

if __name__ == "__main__":
    app.run(debug=True)