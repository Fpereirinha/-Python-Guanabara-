# matrizes
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    print()
