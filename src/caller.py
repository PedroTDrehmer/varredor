from src.factory.listar_empresas import listar_empresas
from src.factory.criar_relatorio import criar_relatorio


class Caller:

    def call(self):
        criar_relatorio()
        listar_empresas()
