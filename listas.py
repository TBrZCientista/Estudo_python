frutas = ["laranja", "maçã", "uva"]

frutas_a = []

letras = list("python") # ele gerará uma lista separando cada letra como um objeto dela

numeros = list(range(10)) #criará uma lista de 0 a 9. "range = builtin"

carro = ["Ferrari","F8", 4200000, 2020, 2900, "São Paulo", True]

print(frutas)
print(frutas_a)
print(letras)
print(numeros)
print(carro)

print(frutas[2]) #selecionando item da lista pelo índice
print(letras[-4]) #selecionando o item do final para o começo, índice começa por -1

#matriz

matriz = [
    [1, "a", 2],
    ["b",3 , 4],
    [6, 5, "c"]
]

print(matriz[0]) #pega a primeira linha inteira
print(matriz[0][0]) #pega o primeiro item da primeira linha
print(matriz[0][-1]) #pega o último item da primeira linha
print(matriz[-1][-1]) #pega o último item da última linha

#fatiamento

lista = ["p","y","t","h","o","n"]

print(lista[2:]) #contagem começará do índice 2. ([início:fim-1:passos])
print(lista[:2]) #a contagem irá até o índice 1
print(lista[1:3]) #começa no índice 1 e vai até o índice 2
print(lista[0:3:2]) #começa no índice 0, vai até o índice 2, conta de 2 em 2
print(lista[::]) #como não tem nada declarado, pega cada ítem da lista em ordem crescente
print(lista[::-1]) #como colocou os passos começando do -1, pega a lista inteira em ordem decrescente

#iteração de listas

carros = ["gol", "celta", "palio"]

for carro in carros: #carro, simboliza cada item da lista.
    print(carro)

#função enumerate

carros_1 = ["gol", "celta", "palio"]

for indice, carro_1 in enumerate(carros_1): #enumera os itens da lista
    print(f"{indice}: {carro_1}")

#compressão de listas

#1ª maneira

numeros_1 = [1, 23, 46, 55, 657, 2]
pares = []

for numero_1 in numeros_1:
    if numero_1 % 2 == 0:
        pares.append(numero_1)

print(pares)

#2ª maneira

numeros_2 = [1, 2, 4, 5, 6, 8, 0]

pares_1 = [numero_2 for numero_2 in numeros_2 if numero_2 % 2 == 0]

print(pares_1)

#modificando valores. 1ª forma

numeros_3 = [1, 3, 5, 6, 8, 0]
quadrado = []

for numero_3 in numeros_3:
    quadrado.append(numero_3 ** 2)

print(quadrado)

#modificando valores. 2ª forma

numeros_4 = [1, 3 , 5, 6, 7, 8, 45]

quadrado_1 = [numero_4 ** 2 for numero_4 in numeros_4]

print(quadrado_1)