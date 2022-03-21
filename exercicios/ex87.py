# matrizes
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somapar = 0
x = int(input('Qual o tamanho da matriz que deseja ? o número sera a mesma quantidade de colunas e linhas'))
geral = []
for escolha in range(x):
    geral.append([])
for linha in range(x):
    for coluna in range(x):
        geral[linha].append(int(input(f'Digite o valor para [{linha}, {coluna}]')))
for d in range(x):
    for e in range(x):
        print(f'[{geral[d][e]:^10}]', end='')
        if geral[d][e] % 2 == 0:
            somapar += geral[d][e]
        if e == 2:
            soma += geral[d][e]
    print()
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'A soma dos valores pares é {somapar}.')
print(f'O maior valor da segunda coluna é {max(geral[1])}')
