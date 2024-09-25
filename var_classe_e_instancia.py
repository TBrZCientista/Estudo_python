class Estudante:
    escola = "Auto ditata"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Felipe", 1)
aluno_2 = Estudante("Théo", 2)

mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Casa"
aluno_3 = Estudante("Fabiana", 3)
aluno_3.escola = "Escola"
mostrar_valores(aluno_1, aluno_2, aluno_3)