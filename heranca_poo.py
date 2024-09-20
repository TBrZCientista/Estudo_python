#herança simples

class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligar o motor!!")

    def __str__(self):
        return self.cor


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) #o super é utilizado para chamar a implementação da classe Pai
        self.carregado = carregado
    
    def esta_carregado(self): #declaração de algo específico para a classe herdeira
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("Azul", "ABC-3456", 2)
moto.ligar_motor()

carro = Carro("Branco", "HGT-0987", 4)
carro.ligar_motor()

caminhao = Caminhao("verde","WDR-6754", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(caminhao)