import os
import pandas as pd

PATH_ARQUIVOS = 'C:\\Users\\Nexxo\\HubNexxo\\HubNexxo - Arquivos - zRobo\\zRoboNotaSalvador\\11 - 2024'
PATH_SAVE = 'C:\\Users\\Nexxo\\HubNexxo\\HubNexxo - Arquivos - zRobo\\RELATÓRIO_RETENÇÕES'

DATA_FRAME = []

# Percorre todas as pastas na pasta principal
for nome_pasta in os.listdir(PATH_ARQUIVOS):
    caminho_pasta = os.path.join(PATH_ARQUIVOS, nome_pasta)
    print(nome_pasta)

    # Verifica se é uma pasta
    if os.path.isdir(caminho_pasta):

        # Percorre os arquivos dentro da pasta
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.startswith("Recebidas") and arquivo.endswith(".csv"):  # Verifica o nome e extensão
                caminho_arquivo = os.path.join(caminho_pasta, arquivo)

                # Lê o CSV
                df = pd.read_csv(caminho_arquivo, encoding='ISO-8859-1', sep=';', on_bad_lines='skip')

                colunas = ['PIS', 'COFINS', 'INSS', 'IRPJ', 'CSLL']
                resultados = [nome_pasta]  # Adiciona o nome da pasta (empresa)

                for coluna in colunas:
                    if coluna in df.columns:  # Verifica se há coluna
                        df[coluna] = df[coluna].astype(str).str.replace(',', '.', regex=False).astype(float)  # Corrige formato
                        soma = df[coluna].sum()  # Soma os valores
                        resultados.append(soma)  # Adiciona a soma à lista
                    else:
                        resultados.append(0.0)  # Se a coluna não existir, adiciona 0.0

                DATA_FRAME.append(resultados)

        # Cria o DataFrame com todos os resultados
        df_resultado = pd.DataFrame(DATA_FRAME, columns=['EMPRESA', 'PIS', 'COFINS', 'INSS', 'IRPJ', 'CSLL'])

# Salva o resultado no Excel
caminho_excel = os.path.join(PATH_SAVE, 'Relatorio.xlsx')
df_resultado.to_excel(caminho_excel, index=False)
print('RELATORIO CONCLUIDO')
