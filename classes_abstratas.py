from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod    
    def desligar(self):
        pass

    @property 
    @abstractmethod
    def marca(self):
        pass

class Controle_tv(Controle_remoto):
    def ligar(self):
        print("Ligando a TV.")
        print("Tv ligada.")

    def desligar(self):
        print("Desligando a TV.")
        print("Tv desligada.")
    
    @property
    def marca(self):
        return "Samsung"

#quando uma classe implementa um método de uma classe abstrata, ele tem que implementar obrigatóriamente implementar os métodos abstratos

class Controle_ar_condicionado(Controle_remoto):
    def ligar(self):
        print("Ligando o Ar Condicionado.")
        print("Ar ligado.")

    def desligar(self):
        print("Desligando o Ar Condicionado.")
        print("Ar desligado.")

    @property
    def marca(self): #se não colocar o @property o código não mostra no print
        return "Samsung"

controle = Controle_tv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = Controle_ar_condicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

