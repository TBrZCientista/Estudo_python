# set é um conjunto de elementos únicos.

print(set([1,1,3,4,5,5,6,7,7,])) #utilizando o set, a gente só mostra os ítens, sem repetição

#acima uma lista

print(set("abobora")) #o retorno do set, não necessáriamente vem em ordem.

#acima uma tupla

linguagens = {"python", "python", "HTML"} #o set também pode ser chamado declarando a váriavel, e os valores entre chaves

print(linguagens) 

#o exemplo acima é praticamente inutilizado

#para consumir os dados do set, é necessário convertê-lo em lista

numeros = {1,1,2,2,3,3,4,4,5,5,}

numeros = list(numeros) #conversão em lista

print(numeros[2]) #acessando o índex 2

#iterar

pokemons = {"pikachu", "gengar", "bulbasaur", "chicorita"}

for pokemon in pokemons:
    print(pokemon)

#enumerar

pokemons = {"pikachu", "gengar", "bulbasaur", "chicorita"}

for indice, pokemon in enumerate(pokemons):
    print(f"{indice}:{pokemon}")

#agora os métodos em SET

#{}.union

conjunto_1 = {1, 2}
conjunto_2 = {3,4}

print(conjunto_1.union(conjunto_2))

#{}.intersection (intercessão)

conjunto_3 = {1, 2, 3, 4}
conjunto_4 = {2,3,4,5}

print(conjunto_3.intersection(conjunto_4))

#{}.difference (diferença)

conjunto_3 = {1, 2, 3, 4}
conjunto_4 = {2,3,4,5}

print(conjunto_3.difference(conjunto_4))
print(conjunto_4.difference(conjunto_3))

#{}.symmetric_difference (diferença simétrica)

conjunto_3 = {1, 2, 3, 4}
conjunto_4 = {2,3,4,5}

print(conjunto_3.symmetric_difference(conjunto_4)) #retorna o que os dois conjuntos tem de diferente um do outro

#{}.issubset (subconjunto)

conjunto_5 = {1, 2, 3, 4, 5, 6}
conjunto_6 = {2,3,4,5}

print(conjunto_5.issubset(conjunto_6))
print(conjunto_6.issubset(conjunto_5))

#{}.issuperset (estão contidos)

conjunto_5 = {1, 2, 3, 4, 5, 6}
conjunto_6 = {2,3,4,5}

print(conjunto_5.issuperset(conjunto_6))
print(conjunto_6.issuperset(conjunto_5))

#{}.isdisjoint (não estão contidos, não existe intercessão)

conjunto_5 = {1, 2, 3, 4, 5, 6}
conjunto_6 = {2,3,4,5}
conjunto_7 = {7, 8, 9, 0}

print(conjunto_5.isdisjoint(conjunto_6))
print(conjunto_6.isdisjoint(conjunto_5))
print(conjunto_5.isdisjoint(conjunto_7))

#{}.add (adicona i item caso ele não exista no conjunto(SET))

sorteio = {1, 3}

sorteio.add(2)

print(sorteio)

#{}.clear

sorteio = {1, 3}

print(sorteio)

sorteio.clear()

print(sorteio)

#{}.copy

sorteio = {1, 3}

print(sorteio)

sorteio.copy()

print(sorteio)

#{}.discard (descarta um valor do conjunto, contando que este exista no conjunto)

numeros_1 = {0,1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(numeros_1)

numeros_1.discard(1)

print(numeros_1)

numeros_1.discard(2)

print(numeros_1)

#{}.pop (retira o índice do conjunto, do menor para o maior)

numeros_1 = {0,1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(numeros_1)

numeros_1.pop()

print(numeros_1)

#{}.remove (remove do conjunto o ítem passado, caso não exista, dá um erro)

numeros_1 = {0,1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(numeros_1)

numeros_1.remove(2)

print(numeros_1)

#{}.len (mostra a quantidade de ítens no conjunto)

numeros_1 = {0,1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(len(numeros_1))

#{}.in (mostra se o item solicitado faz parte do grupo)

numeros_2 = {0,1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(1 in numeros_2)
print(45 in numeros_2)

#{}.