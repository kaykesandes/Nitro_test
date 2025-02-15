import pandas as pd
import matplotlib.pyplot as plt

import os
os.makedirs('App/solucao', exist_ok=True)


def generate_powerbi_report(df, total_faturado, total_faturado_loja1, total_faturado_loja2, total_faturado_loja3, top_vendedores_loja1, top_vendedores_loja2, top_vendedores_loja3, soma_total_faturado):
    # Create a summary DataFrame
    summary_data = {
        'Total Faturado': [total_faturado],
        'Total Faturado Loja 1': [total_faturado_loja1],
        'Total Faturado Loja 2': [total_faturado_loja2],
        'Total Faturado Loja 3': [total_faturado_loja3],
        'Soma Total Faturado': [soma_total_faturado]
    }
    summary_df = pd.DataFrame(summary_data)

    # Save summary to Excel
    summary_df.to_excel('App/solucao/powerbi_summary.xlsx', index=False)

    # Save top vendedores to Excel
    with pd.ExcelWriter('App/solucao/powerbi_top_vendedores.xlsx') as writer:
        top_vendedores_loja1.to_excel(writer, sheet_name='Top Vendedores Loja 1', index=False)
        top_vendedores_loja2.to_excel(writer, sheet_name='Top Vendedores Loja 2', index=False)
        top_vendedores_loja3.to_excel(writer, sheet_name='Top Vendedores Loja 3', index=False)

    # Generate and save plots

    print("Excel report generated successfully.")