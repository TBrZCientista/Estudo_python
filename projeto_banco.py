#projeto banco

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

menu = """

### Seja bem vindo ao Banco Freitas.###
    Selecione uma opção abaixo:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

=> """

while True:

    opção = input(menu)

    if opção == "1":
        
        valor = float(input("Informe o valor à depositar por favor: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Erro na operação. Valor informado é inválido")
    
    elif opção == "2":
        
        valor = float(input("Informe o valor à sacar por favor: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Falha na operação. Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Falha na operação. O valor solicitado é maior que seu limite.")

        elif excedeu_saques:
            print("Falha na operação. Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1

        else:
            print("Falha na operação. O valor informado é inválido.")

    elif opção == "3":
        print("\n########## Extrato ##########")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#############################")

    elif opção == "0":
        break

    else:
        print("Opção inválida. Por favor, selecione uma das operações do Menu.")