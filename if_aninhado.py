conta_normal = False
conta_universitaria = False
conta_prime = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso. Aguarde enquanto contamos as cédulas.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial. Aguarde enquanto contamos as cédulas")
    else:
        print("Não foi possível realizar seu saque, saldo insuficiente.")  

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso. Aguarde enquanto contamos as cédulas.")
    else:
        print("Saldo insuficiente.")

elif conta_prime:
    print("Conta Prime selecionada. Seja bem vindo!!!")
    
else:
    print("Sistema não reconheceu seu tipo de conta. Entre em contato com seu Gerente.")