#[].append. (acrescenta algo na lista criada)

lista = []

lista.append(1) 
print(lista)

lista.append("Python")
print(lista)

lista.append([40, 30, 20])

print(lista)

#[].clear. Limpa a lista criada

lista_1 = []

lista_1.append(1) 
lista_1.append("Python")
lista_1.append([40, 30, 20])

print(lista_1)

lista_1.clear()

print(lista_1)

#[].copy . Ele evita a alteração na lista original

lista_2 = [1, "python", [49, 30, 20]]

lista_2.copy()

print(lista_2)

#[].count . Conta quantas vezes o item se repete na lista

cores = ["vermelho", "azul", "amarelo","cinza", "laranja", "amarelo"]

print(cores.count("vermelho"))
print(cores.count("amarelo"))

#[].extend. Utilizado quando eu quero acrescentar mais itens na lista, juntando mais de um item

linguagens = ["python", "java", "C+"]

print(linguagens)

linguagens.extend(["js", "C"])

print(linguagens)

#[].index . Retorna a primeira ocorrência do item informado

linguagens_1 = ["python", "java", "C+"]

print(linguagens_1.index("python"))
print(linguagens_1.index("java"))

#[].pop . Por padrão, retira o último ítem adicionado na lista

linguagens_2 = ["python", "java", "C+", "HTML", "js"]

print(linguagens_2.pop())
print(linguagens_2.pop())
print(linguagens_2.pop(1))
print(linguagens_2.pop(0))

#[].remove . Retira da lista o item informado.

linguagens_3 = ["python", "java", "C+", "HTML", "js"]

linguagens_3.remove("C+")

print(linguagens_3)

#[].reverse . Retorna os itens da lista do final para o começo

linguagens_4 = ["python", "java", "C+", "HTML", "js"]

linguagens_4.reverse()

print(linguagens_4)

#[].sort . Ele ordena a lista de acordo com os parametros passados

linguagens_5 = ["python", "java", "C+", "HTML", "js"]
linguagens_5.sort()

print(linguagens_5)

linguagens_5 = ["python", "java", "C+", "HTML", "js"]
linguagens_5.sort(reverse=True)

print(linguagens_5)

linguagens_5 = ["python", "java", "C+", "HTML", "js"]
linguagens_5.sort(key=lambda x:len(x)) #lambda função anônima, quando tem coisas com o mesmo tamanho, aparece primeiro quem estiver primeiro no código

print(linguagens_5)

linguagens_5 = ["python", "java", "C+", "HTML", "js"]
linguagens_5.sort(key=lambda x:len(x), reverse=True)

print(linguagens_5)

#.len . Retorna a quantidade de índices informados

linguagens_5 = ["python", "java", "C+", "HTML", "js"]

print(len(linguagens_5))

#.sorted

linguagens_5 = ["python", "java", "C+", "HTML", "js"]

print(sorted(linguagens_5, key=lambda x:len(x))) #também aceita o parâmetro Reversed

