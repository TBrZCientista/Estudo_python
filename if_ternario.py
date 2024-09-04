saldo = 1000
saque = int(input("Informe o valor do saque: "))

status = "Sucesso" if saldo >= saque else "Falha"

print (f"{status} ao realizar o saque.")