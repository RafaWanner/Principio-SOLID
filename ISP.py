from abc import ABC, abstractmethod

class Impressora(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Digitalizadora(ABC):
    @abstractmethod
    def digitalizar(self):
        pass

class Multifuncional(Impressora, Digitalizadora):
    def imprimir(self):
        print("Imprimindo")
    
    def digitalizar(self):
        print("Digitalizando")

class ImpressoraSimples(Impressora):
    def imprimir(self):
        print("Imprimindo")

# Uso
impressora = ImpressoraSimples()
impressora.imprimir()