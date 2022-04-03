from Modulos.Numeros import menu, leiaInt
from time import sleep
from Modulos.Strings import titulo
from Modulos.arquivo import *


arq = 'Pessoas.txt'
if not arquivoExiste(arq):
    criarArq(arq)


dados = {}
while True:
    resp = menu(['Cadastrar Pessoa', 'Ver Pessoas', 'Sair do Programa'])
    if resp == 1:
        titulo('Opção 1')
        dados['Nome'] = str(input('Digite o nome:')).strip()
        dados['Idade'] = leiaInt('Idade: ')
        dados['Sexo'] = str(input('Qual o sexo ? [M/F]')).strip().upper()[0]
        while dados['Sexo'] not in 'MF':
            dados['Sexo'] = str(input('Qual o sexo ? [M/F]')).strip().upper()[0]
        for valor in dados.values():
            outfile = open(arq, 'at')
            outfile.writelines(f'{str(valor):<25}')
            outfile.close()
        outfile = open(arq, 'at')
        outfile.writelines(f'\n')
        outfile.close()
        dados.clear()
    elif resp == 3:
        titulo('Opção 3')
        titulo('Saindo do Sistema, até logo')
        break
    elif resp == 2:
        titulo('Opção 2')
        print(f'{"|NOME|":<21} {"|IDADE|":<25} {"|SEXO|"}')
        infile = open(arq, 'rt')
        print(infile.read())
        infile.close()
    else:
        print('Tente novamente, opção invalida.')
    sleep(2)
