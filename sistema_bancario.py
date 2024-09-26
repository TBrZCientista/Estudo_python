from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class Pessoa_fisica(Cliente):
    def __init__(self,nome, data_de_nascimento,cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    @abstractmethod
    def nova_conta(cls,cliente, numero):
        return cls(numero, cliente)
    
    @property
    @abstractmethod
    def saldo(self):
        return self._saldo
    
    @property
    @abstractmethod
    def numero(self):
        return self._numero
    
    @property
    @abstractmethod
    def agencia(self):
        return self._agencia
    
    @property
    @abstractmethod
    def cliente(self):
        return self._cliente
    
    @property
    @abstractmethod
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n### A sua operação falhou!!! Você não possui saldo suficiente.###")

        elif valor > 0:
            self._saldo -= valor
            print("\n### Seu saque foi realizado com sucesso!!!###")
            return True
        
        else:
            print("\n### O valor informado é inválido. Falha na operação!!!###")

        return False
    
    def depositar(self, valor):

        if valor > 0:
            self._saldo += valor
            print("\n### Seu depósito foi realizado.")

        else:
            print("\n### Falha na operação. O valor informado é inválido.###")
            return False
        
        return True    

class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite = 500,limite_de_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_de_saque = limite_de_saque

    def sacar(self, valor):
        numero_de_saques = len(
            [transacao for transacao in self.historico.transacoes 
            if transacao["tipo"]== Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_de_saques >= self.limite_de_saque

        if excedeu_limite:
            print("\n### Falha na operação. O valor do saque ultrapassou o limite disponível")
        
        elif excedeu_saques:
            print("\n### Falha na operação. Máximo de saques do dia alcançado.###")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    @abstractmethod
    def transacoes(self):
        return self.transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:$s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    @abstractmethod
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

        @property
        @abstractmethod
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)

            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)

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

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n### Cliente não possui conta!###")
        return
    
    # DISCLAIMER = O CLIENTE NÃO PODE ESCOLHER A CONTA
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n### Cliente não encontrado###")
        return
    
    valor = float(input("Informe o valor do depósito por favor:"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n### Cliente não encontrado.###")
        return
    
    valor = float(input("Informe o valor do saque por favor: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n### Cliente não encontrado. ###")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n########## Extrato ##########")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas operações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao["tipo"]}:\n\tR${transacao["valor"]:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("#############################")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n### Criação de conta encerrada. ###")
        return
    
    conta = Conta_corrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n### Conta criada com sucesso###")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n### Já existe cliente com esse CPF. ###")
        return
    
    nome = input("Informe o nome completo: ")
    data_de_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe seu endereço por favor (Logradouro, número, bairro, cidade/sigla estado)")

    cliente = Pessoa_fisica(nome=nome, data_de_nascimento=data_de_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n### Cliente criado com sucesso. ###")


def main():
    clientes = []
    contas = []


    while True:

        opção = menu()

        if opção == "1": #opção de depósito
            
            depositar(clientes)
        
        elif opção == "2": #opção de saque
            
            sacar(clientes)
            
        elif opção == "3": #opção de extrato
            
            exibir_extrato(clientes)

        elif opção == "4": #opção de Criar nova conta

            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        
        elif opção == "5": #opção de listar contas

            listar_contas(contas)

        elif opção == "6": #opção de criar novo usuário

            criar_cliente(clientes)

        elif opção == "0": #opção de saída do sistema
            print("Muito obrigado por utilizar os serviços do Banco Freitas!!!")
            break

        else: #caso selecione algo diferente da opção, a mensagem abaixo aparece
            print("Opção inválida. Por favor, selecione uma das operações do Menu.")

main()