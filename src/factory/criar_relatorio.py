import os
import pandas as pd
from env import PATH_ARQUIVOS, PATH_SAVE
from src.library.date import date


def criar_relatorio():
    DATA_FRAME = []

    # Percorre todas as pastas na pasta principal
    for empresa in os.listdir(PATH_ARQUIVOS):
        caminho_pasta = os.path.join(PATH_ARQUIVOS, empresa)

        # Verifica se é uma pasta
        if os.path.isdir(caminho_pasta):

            # Percorre os arquivos dentro da pasta
            for arquivo in os.listdir(caminho_pasta):

                # Verifica o nome e extensão
                if arquivo.startswith("Recebidas") and arquivo.endswith(".csv"):  
                    caminho_arquivo = os.path.join(caminho_pasta, arquivo)
                    
                    # Lê o CSV
                    df = pd.read_csv(caminho_arquivo, encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
                    
                    colunas = ['PIS', 'COFINS', 'INSS', 'IRPJ', 'CSLL']

                    # Percorre o CSV
                    for _, linha in df.iterrows():
                        nfse = linha['Nº NFS-e']

                        # Percorre as colunas
                        for coluna in colunas:
                            if linha[coluna] != '0,00' and not pd.isna(linha[coluna]):
                                DATA_FRAME.append([empresa, nfse, linha['PIS'], linha['COFINS'], linha['INSS'], linha['IRPJ'], linha['CSLL']])
                
            # Criação do DataFrame final
            df_resultado = pd.DataFrame(DATA_FRAME, columns=['EMPRESA', 'Nº NFS-e', 'PIS', 'COFINS', 'INSS', 'IRPJ', 'CSLL'])

    # Salva o resultado no Excel
    caminho_excel = os.path.join(PATH_SAVE, f'RELATORIO {date()}.xlsx')
    df_resultado.to_excel(caminho_excel, index=False)
    print('RELATORIO CRIADO')