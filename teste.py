def analise_vendas(vendas):

    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():

    entrada = input()
    entrada = entrada.split()
    entrada = list(map(int, entrada))
    vendas = entrada

    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))