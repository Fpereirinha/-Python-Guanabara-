'''dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados['sexo'])
for k, v in dados.items():
    print(k, end= ' ')
    print(v)'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'Sãopaulo ', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
for estados in brasil:
    for k, v in estados.items():
        print(f'{k} = {v}')'''
estado = {}
brasil = []
for c in range(3):
    estado['UF'] = str(input(f'Digite o nome do {c+1}° UF:'))
    estado['Sigla'] = str(input(f'Digita a sigla do {c+1}° UF:'))
    brasil.append(estado.copy())
    estado.clear()
for contador, estados in enumerate(brasil):
    for key, value in estados.items():
        print(f'O {contador+1}° {key} é {value}')

