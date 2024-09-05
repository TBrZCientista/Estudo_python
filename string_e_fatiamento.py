#métodos úteis para strings
curso = "pYtHon"

print(curso.upper()) #todas as letras maiúsculas
print(curso.lower()) #todas as letras minúsculas
print(curso.title()) #transforma a palavra num título

curso = "    Python "

print(curso.strip())  #retira todos os espaços tanto a direita quanto da esquerda da string
print(curso.lstrip()) #retira os espaços do lado esquerdo da string
print(curso.rstrip()) #retira os espaços do lado direito da string

curso = "Python"

print(curso.center(10,"#")) #utiliza dois argumentos, nºde caracteres e o caracter que será utilizado no espaço.
print(".".join(curso)) #usado para juntar iteráveis

