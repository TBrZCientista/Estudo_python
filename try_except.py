try:
    open('config.txt')
except FileNotFoundError:
    print("Não foi encontrado o arquivo config.txt!!!")