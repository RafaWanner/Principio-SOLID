from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14 * self.raio ** 2

def imprimir_area(forma: Forma):
    print(f"Área: {forma.calcular_area()}")

# Uso
retangulo = Retangulo(10, 5)
circulo = Circulo(7)
imprimir_area(retangulo)  # Área: 50
imprimir_area(circulo)    # Área: 153.86