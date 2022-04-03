def arquivoExiste(x):
    try:
        a = open(x, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(x):
    try:
        open(x,'wt+')
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {x} criado com sucesso.')
    finally:
        print('Arquivo ja criado.')


def cadastrar(arq, x):
    try:
        open(arq, 'at')
    except:
        print('Erro na abertura de arquivo.')
    else:
        open(arq, 'at').write(x)

