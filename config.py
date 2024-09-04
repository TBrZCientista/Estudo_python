def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Não foi encontrado o arquivo config.txt!")
    except IsADirectoryError:
        print('O arquivo config.txt foi encontrado, mas é um diretório, não conseguimos lê-lo.')
    except (BlockingIOError, TimeoutError):
        print("O sistema de arquivos está sobrecarregado, não conseguimos carregar o arquivo de configuração")

if __name__ == '__main__':
    main()