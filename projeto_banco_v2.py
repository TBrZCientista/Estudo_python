#projeto banco V2

import textwrap

def menu():
    menu = """\n

    ### Seja bem vindo ao Banco Freitas.###
        Selecione uma opção abaixo:

        [1]\t Depositar
        [2]\t Sacar
        [3]\t Extrato
        [4]\t Nova Conta
        [5]\t Listar Contas
        [6]\t Novo Usuário
        [0]\t Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Erro na operação. Valor informado é inválido.")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_de_saques,LIMITE_DE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

    if excedeu_saldo:
        print("\n Falha na operação. Você não possui saldo suficiente.")

    elif excedeu_limite:
        print("\n Falha na operação. O valor solicitado é maior que seu limite.")

    elif excedeu_saques:
        print("\n Falha na operação. Número de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_de_saques += 1
        print("\n Saque realizado com sucesso.")

    else:
        print("Falha na operação. O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print("\n########## Extrato ##########")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("#############################")

def criar_usuario(usuarios):

    cpf = input("Informe o CPF (Somente Números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!!!")

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_da_conta, usuarios):

    cpf = input(" Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!!!")
        return{"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": usuario}
    
    print("\n Usuário não encontrado, processo de criação de conta abortado.")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C: \t\t{conta['numero_da_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:

        opção = menu()

        if opção == "1": #opção de depósito
            
            valor = float(input("Informe o valor à depositar por favor: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opção == "2": #opção de saque
            
            valor = float(input("Informe o valor à sacar por favor: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_de_saques = numero_de_saques,
                LIMITE_DE_SAQUES = LIMITE_DE_SAQUES,
            )
            
        elif opção == "3": #opção de extrato
            
            exibir_extrato(saldo, extrato=extrato)

        elif opção == "4": #opção de Criar nova conta

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opção == "5": #opção de listar contas

            listar_contas(contas)

        elif opção == "6": #opção de criar novo usuário

            criar_usuario(usuarios)

        elif opção == "0": #opção de saída do sistema
            print("Muito obrigado por utilizar os serviços do Banco Freitas!!!")
            break

        else: #caso selecione algo diferente da opção, a mensagem abaixo aparece
            print("Opção inválida. Por favor, selecione uma das operações do Menu.")

main()