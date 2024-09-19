class bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro = 18): #self é a instância do objeto que foi passado. (__init__ é um método construtor)
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self): #essa declaração é um método, é uma fução dentro de uma classe
        print("Píí, piíí") #temos que passar um primeiro argumento. Chamado e argumento posicional

    def parar(self):
        print("Parando a bicicleta.")
        print("Bicicleta parada!!!")

    def correr(self):
        print("Correndo com a bicicleta")

    def __str__(self): 
        return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor} "

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

monark = bicicleta("azul", "monark", 2024, 450)

monark.buzinar()
monark.correr()
monark.parar()

print(monark.ano, monark.cor, monark.modelo, monark.valor) #acessando os atributos
print(monark)