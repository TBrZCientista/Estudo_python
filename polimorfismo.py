class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):#classe filha de Passaro
    def voar(self):
        super().voar()

class Avestruz(Passaro):#classe filha de Passaro
    def voar(self):
        print("Avestruz não voa.")

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)