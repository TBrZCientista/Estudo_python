#tuplas não podem ser alteradas

frutas = ("laranja","pêra", "uva", "melancia",)

print(frutas)
print(frutas[2]) #acessando diretamente o índice na tupla
print(frutas[-3]) 

letras = tuple("freitas")

print(letras)

numeros = tuple([1, 2, 3, 4])

print(numeros)

pais = ("Brasil",)

print(pais)

#tuplas aninhadas

matriz = (
    (1, "a", 2),
    ("v",6, 9),
    (5, 3, "ed")
)

print(matriz[0])
print(matriz[0][1])

#fatiamento

tupla = ("f","r","e","i","t","a","s")

print(tupla[2:])
print(tupla[:2])
print(tupla[1:5:2])
print(tupla[::-1])

#iteração

carros = ("corolla", "monza", "fusca", "tipo")

for carro in carros:
    print(carro)

#enumerate

carros_1 = ("corolla", "monza", "fusca", "tipo")

for indice, carro in enumerate(carros_1):
    print(f"{indice}: {carro}")

#métodos

#().count

cores = ("vermelho", "azul marinho", "cinza", "amarelo", "lilás","vermelho")

print(cores.count("vermelho"))
print(cores.count("lilás"))

#().index

linguages = ("Phyton", "C+", "Java", "HTML")

print(linguages.index("HTML"))

#().len

linguages = ("Phyton", "C+", "Java", "HTML")

print(len(linguages))

carros_3 = ("gol")

print(isinstance(carros,tuple))