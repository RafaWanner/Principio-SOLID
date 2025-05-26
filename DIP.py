from abc import ABC, abstractmethod

class BancoDeDados(ABC):
    @abstractmethod
    def salvar(self, dados):
        pass

class MySQL(BancoDeDados):
    def salvar(self, dados):
        print(f"Salvando {dados} no MySQL")

class MongoDB(BancoDeDados):
    def salvar(self, dados):
        print(f"Salvando {dados} no MongoDB")

class ServicoRelatorio:
    def __init__(self, banco: BancoDeDados):
        self.banco = banco
    
    def gerar_relatorio(self, relatorio):
        self.banco.salvar(relatorio)

# Uso
servico = ServicoRelatorio(MongoDB())
servico.gerar_relatorio("Relatório Mensal")