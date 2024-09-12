pessoa = {"nome": "felipe freitas", "idade": 37} #dicionário com "chave : valor". 1ª forma

print(pessoa)

pessoa_2 = dict(nome = "Felipe Freitas", idade = "37") # segunda forma. Usando a classe dict

print(pessoa_2)

pessoa_2["telefone"] = "21-999634468" #utilizado quando se quer acrescentar alguma coisa no dicionário

print(pessoa_2)

#acessando dados dentro do dicionário

dados = {"nome": "Felipe Freitas","idade": 37,"telefone": "21999634468"}

print(dados["nome"]) #usa-se o índice desejado como declaração
print(dados["idade"])
print(dados["telefone"])

#sobreescrevendo dados na chave

dados["nome"] = "Fabiana Coelho" #declara-se a chave, e atribui-se o novo valor desejado
dados["idade"] = 36
dados["telefone"] = "21996785554"

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

#dicionários aninhados

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

telefone = contatos["biadolipef@hotmail.com"]["telefone"]

print(telefone)

#iteração de dicionários

for chave in contatos:
    print(chave,contatos[chave]) #não é a melhor maneira



for chave, valor in contatos.items():
    print(chave, valor)

#métodos da classe dict

#{}.clear

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

contatos.clear()
print(contatos)

#{}.copy

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

copia = contatos.copy()
copia["felipefreitasdaschagas@hotmail.com"] = {"nome": "Felipe"}

print(contatos["felipefreitasdaschagas@hotmail.com"])
print(f"Segue a cópia dos dados solicitados: ",copia["felipefreitasdaschagas@hotmail.com"])

#{}.fromkeys cria chaves para a gente.

print(dict.fromkeys(["nome", "telefone"])) #quando não colocamos o valor da chave, retora "None"
print(dict.fromkeys(["nome", "telefone"], "Vazio"))

#{}.get

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

# contatos["chave"] = declarando assim dá erro

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("felipefreitasdaschagas@hotmail.com", {}))

#{}.items . retorna os itens do dicionário como lista de tuplas

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
}

print(f"Essas são as chaves do seu dicionário: ", contatos.items())

#{}.pop . Remove um item do dicionário, e retorna o valor removido

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

print(contatos.pop("felipefreitasdaschagas@hotmail.com"))

print(f"Após a exclusão solicitada, seu dicionário ficou assim: ",contatos)

#caso o item solicitado não exista, você pode declarar um valor padrão para retorno no segundo argumento.
#contatos.pop("frutuoso@gmail.com", {}) Exemplo.

#{}.popitem - retira os itens na sequência

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

resposta = contatos.popitem()
print(resposta)

#{}.setdefault - se o atributo não estiver no dicionário, ele acrescenta com o valor informado

contato = {'nome': 'Felipe', 'telefone': '21999999999'}

print(contato)

contato.setdefault("idade", 37)

print(contato)

#{}.update - Atuaaliza o dicionário com o valor informado

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

contatos.update({"theodesouzafreitas@hotmail.com":{"nome": "Theo de Souza Freitas", "idade": 5}})

print(contatos)

#{}.values - É um método que retorna só os valores das chaves do dicionário

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

print(contatos.values())

#{}.in verifica no dícionário se a chave informada existe. Retornando um valor Booleano

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

print("pituca@gmail" in contatos)
print("felipefreitasdaschagas@hotmail.com" in contatos)
print("idade" in contatos["felipefreitasdaschagas@hotmail.com"]) #verifica se a chave "idade" existe no campo informado do dicionário

#{}del.

contatos={
    "felipefreitasdaschagas@hotmail.com":
        {"nome": "Felipe Freitas", "telefone":"21999634468"},
    "biadolipef@hotmail.com":
        {"nome": "Fabiana Coelho", "telefone": "21996785554"},
}

del contatos["felipefreitasdaschagas@hotmail.com"]["telefone"] #aqui, está sendo removido o índice Telefone da chave felipefreitasdascagas@hotmail.com
del contatos ["biadolipef@hotmail.com"] #aqui está sendo removido a chave inteira
print(contatos)