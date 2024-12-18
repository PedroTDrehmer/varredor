import os
import pandas as pd
from env import PATH_SAVE

def listar_empresas():
    arquivos = sorted(os.listdir(PATH_SAVE), key=lambda f: os.path.getmtime(os.path.join(PATH_SAVE, f)), reverse=True)
    dois_ultimos = arquivos[:2]  # Os dois arquivos mais recentes
    
    empresas_completas = pd.DataFrame()  # DataFrame vazio para armazenar as empresas
    
    for arquivo in dois_ultimos:
        caminho_arquivo = os.path.join(PATH_SAVE, arquivo)
        
        # Lê o arquivo Excel
        df = pd.read_excel(caminho_arquivo)
        
        # Extrai a coluna "EMPRESA"
        empresas = df['EMPRESA']
        
        # Adiciona as empresas ao DataFrame final
        empresas_completas = pd.concat([empresas_completas, empresas], ignore_index=True)

    # Remove empresas duplicadas
    empresas_completas = empresas_completas.drop_duplicates().reset_index(drop=True)
    
    # Salva todas as empresas extraídas em um novo arquivo Excel
    empresas_completas.to_excel(os.path.join(PATH_SAVE, 'EMPRESAS.xlsx'), index=False)

    print('EMPRESAS LISTADAS')
