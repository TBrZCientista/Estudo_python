MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade por favor: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade. Pode tirar a CNH!")

if idade < MAIOR_IDADE:
    print("Você ainda é menor de idade. Não pode tirar a CNH!")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade. Pode tirar a CNH")
else:
    print("Você ainda é menor de idade. Não pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade. Pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Você pode fazer as aulas teóricas, mas ainda não pode fazer as práticas.")
else:
    print("Você ainda é menor de idade. Não pode tirar a CNH")