from src.factory.tratar_relatorio import tratar_relatorio
from src.factory.criar_relatorio import criar_relatorio


class Caller:

    def call(self):
        criar_relatorio()
        tratar_relatorio()
