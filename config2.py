try: 
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("Não foi possível encontrar o arquivo config.txt")
    elif err.errno == 13:
        print("O arquivo config.txt foi encontrado mas não consegimos lê-lo")