#conhecendo os métodos __init__ e __del__

class Cachorro:
    def __init__(self, nome, cor, acordado = True): #contrutor
        print("Inicalizando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self): #destrutor
        print("Removendo a instância da classe.")

    def falar(self):
        print("au au")

def criar_cachorro():
    c = Cachorro("Simba", "marrom", False)
    print(c.nome)

criar_cachorro()
c = Cachorro ("Doguinho", "caramelo")
c.falar()

