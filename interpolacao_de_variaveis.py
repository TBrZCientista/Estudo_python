nome = "Felipe"
idade = 37
profissao = "BackOffice"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Felipe", "idade":37}

print ("Nome: %s Idade: %d" %(nome, idade)) #1º forma. Não muito utilizado

print ("Nome: {} Idade: {}".format(nome, idade)) #2ª forma.
print ("Nome: {1} Idade: {0}".format(idade,nome))

print ("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) #3ª forma, mais utilizada
print ("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}") #forma mais simplificada

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}") #o argumento de 10 é um width e não obrigatório, se não delcarar é igual a zero
