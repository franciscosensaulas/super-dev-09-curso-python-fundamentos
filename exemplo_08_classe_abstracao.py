# exemplo_09_classe_abstracao.py
from abc import ABC, abstractmethod
from math import pi


# (....) herança
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        """
        Toda foram geométrica deverá implementar
        uma função para calcular sua área
        """
        pass


class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        self.raio = raio

    def calcular_area(self) -> float:
        area = pi * self.raio ** 2
        return area

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado

circulo = Circulo(5)
print("Área do círculo: ", circulo.calcular_area())

quadrado = Quadrado(4)
print("Área do quadrado: ", quadrado.calcular_area())
