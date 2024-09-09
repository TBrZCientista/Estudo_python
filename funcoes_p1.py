def exibir_mensagem():
    print("Olá Mundo!!!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

def calcular_total(numeros):
    return sum(numeros) #realiza a soma dos números informados

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print ("Olá mundo!")
    return 42

exibir_mensagem()
exibir_mensagem_2(nome= "Felipe")
exibir_mensagem_3() #Se não for passado algum valor, ele assume o definido na função
exibir_mensagem_3(nome="Teteco")

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3())

#argumentos nomeados(abaixo)

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","Palio",1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat","modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
#O ** é um dicionário usado como argumento