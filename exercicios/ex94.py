pessoas = {}
geral = []
media = homem = 0
while True:
    pessoas['Nome'] = str(input('Qual o nome ?'))
    pessoas['Sexo'] = str(input('Qual o sexo ?')).strip().upper()[0]
    while pessoas['Sexo'] not in 'FM':
        pessoas['Sexo'] = str(input('Qual o sexo ?')).strip().upper()[0]
    pessoas['Idade'] = int(input('Qual a idade ?'))
    geral.append(pessoas.copy())
    media += pessoas['Idade']
    pessoas.clear()
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas cadastradas foram {len(geral)}.')
print(f'A média de idade é {media/len(geral)}.')
for valor in geral:
    if valor['Sexo'] == 'M':
        homem += 1
if homem >= 1:
    print(f'Os homens cadastrados foram: ', end='')
    for valor in geral:
        if valor['Sexo'] == 'M':
            print(valor['Nome'], end=' ')
else:
    print('Não houve homens cadastrados.')
print(f'\nAs pessoas acima da média foram: ')
for valor in geral:
    if valor['Idade'] > media/len(geral):
        print(f'{valor["Nome"]} com {valor["Idade"]} anos')
