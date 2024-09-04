while True:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)

for numero in range(100):

    if numero == 10:
        break #é utilizado para parar o código na condição estabelecida
    print(numero)

for numero in range(100):

    if numero == 8:
        continue #é utilizado para "pular" uma condição estabelecida
    print(numero)