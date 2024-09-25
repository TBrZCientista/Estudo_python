class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod #metodo de classe. Preciso de contexto: uso método de classe.
    def criar_data_nascimento(cls,ano, mês, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod #método estático. Não preciso de contexto: uso método estático.
    def e_maior_idade(idade):
        return idade >= 18

p2 = Pessoa.criar_data_nascimento(1987, 5, 25, "Felipe")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(37))
print(Pessoa.e_maior_idade(17))