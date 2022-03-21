dados = {}
dados['Nome:'] = str(input('Nome: ')).strip()
dados['Média:'] = float(input(f'Média de {dados["Nome:"]}: '))
if dados['Média:'] >= 6:
    dados['Situação:'] = 'Aprovado'
else:
    dados['Situação:'] = 'Recuperação.'
print('-='*30)
for key, valor in dados.items():
    print(f'{key} {valor}')
