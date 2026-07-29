from abc import ABC, abstractmethod


def comer():
    print("asodkoasdk")

class Pai(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def tomar_banho(self):
        pass


class Filha(Pai):
    def comer(self):
        print("Arroz com cenoura e brócoli")


class Filho(Pai):
    pass


judity = Filha()
judity.comer()

enzo = Filho()
enzo.comer()