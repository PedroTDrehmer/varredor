import os
import glob
import pandas as pd
from env import PATH_SAVE


def tratar_relatorio():
    arquivos = glob.glob(os.path.join(PATH_SAVE, "*.xlsx"))  # Busca arquivos .xlsx na pasta
    if not arquivos:
        return None  # Retorna None se não encontrar arquivos
    
    excel = max(arquivos, key=os.path.getmtime)  # Encontra o mais recente

    df = pd.read_excel(excel)
    df = df.drop_duplicates()
    df.to_excel(excel, index=False)
