def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a*2 + b*3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da função é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, test)

op = somar
print(op(1,23))

#escopo global

salario = 2000

def salario_bonus(bonus):
    global salario #GLOBAL É PALAVRA RESERVADA
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)

print(salario_com_bonus)