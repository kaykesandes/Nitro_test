import pandas as pd

def separar_prc_qtd(df):
    # Separar a coluna "Preço Unitário - Qtde" em duas colunas: "Preço Unitário" e "Quantidade"
    df[['Preço Unitário', 'Quantidade']] = df['Preço Unitário - Qtde'].str.split('-', expand=True)
    df['Preço Unitário'] = df['Preço Unitário'].astype(float)
    df['Quantidade'] = df['Quantidade'].astype(int)
    return df

def calcular_valor_venda(df):
    df['ValorVenda'] = df['Preço Unitário'] * df['Quantidade']
    return df

def ordenar_datas(df):
    df = df.sort_values(by="Mes")
    return df

def load_data():
    
    # Carregar dados das lojas
    loja1 = pd.read_excel("App/data/Loja1.xlsx", header=0)
    loja2 = pd.read_excel("App/data/Loja2.xlsx", header=0)
    loja3 = pd.read_excel("App/data/Loja3.xlsx", header=0)
    
    # Remover linhas vazias
    loja1.dropna(how='all', inplace=True)
    loja2.dropna(how='all', inplace=True)
    loja3.dropna(how='all', inplace=True)
    
    loja1 = separar_prc_qtd(loja1)
    loja2 = separar_prc_qtd(loja2)
    loja3 = separar_prc_qtd(loja3)
    
    loja1 = calcular_valor_venda(loja1)
    loja2 = calcular_valor_venda(loja2)
    loja3 = calcular_valor_venda(loja3)
        
    # Concatenar dados das lojas
    lojas = pd.concat([loja1, loja2, loja3], ignore_index=True)
    
    # Carregar dados de produtos
    produtos = pd.read_csv("App/data/Produtos.csv", encoding='latin1', delimiter=';')
    
    # Mesclar dados das lojas com dados de produtos
    df = pd.merge(lojas, produtos, left_on="Código Produto", right_on="Codigo Produto")
    
    # Converter coluna "Data Venda" para o tipo período mensal
    df["Mes"] = pd.to_datetime(df["Data Venda"]).dt.to_period("M")
    
    # Calcular métricas e ordenar os dados
    df = ordenar_datas(df)
    
    return loja1, loja2, loja3, lojas, produtos, df