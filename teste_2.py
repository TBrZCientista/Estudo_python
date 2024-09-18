#não está funcionando certo ainda


def produto_mais_vendido(produtos):
    contagem = {}

    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0

    for produto, count in contagem.items():
        while max_count < count:
            max_count += 1

        if max_count == count:
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    entrada = input()
    entrada = entrada.split(",")
    entrada = [item.strip() for item in entrada]
    produtos = entrada

    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))