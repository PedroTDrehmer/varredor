import os
import openpyxl


def varredor():

    caminho = "C:\\Users\\Nexxo\\HubNexxo\\HubNexxo - Arquivos - zRobo\\zRoboNotaSalvador\\11 - 2024"

    pastas_empresas = [nome for nome in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, nome))]


    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Empresas"

    for i, empresa in enumerate(pastas_empresas, start=1):
        ws.cell(row=i, column=1, value=empresa)

    wb.save("empresas_listadas.xlsx")