from abc import ABC, abstractmethod

class Hospedagem(ABC):
    def __init__(self, noites):
        self.noites = noites

    @abstractmethod
    def diaria(self):
        pass

class Chale(Hospedagem):
    def diaria(self):
        return 250
    
c = Chale(2)
h = Hospedagem(3)
print(c.diaria() * c.noites)