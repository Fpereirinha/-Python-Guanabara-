midade = 0
maioridadehomem = 0
nomevelho = ''
femi = 0
femnv = 0
maiorif = 0
femtot = 0
quantidade = int(input('Qual a quantidade de pessoas a serem analisadas ? \n '))
for p in range(1,quantidade + 1):
    print(f'{"="*5} {p}° Pessoa {"="*5}')
    nome = str(input(f'Qual o nome da {p}° pessoa ?')).strip()
    idade = int(input(f'Qual a idade da {p}° pessoa ?'))
    sexo = str(input(f'Qual o sexo da {p}° pessoa ? M / F')).strip()
    midade += idade
    if p == 1 and sexo in 'Ff':
        maiorif = idade
        femnv = idade
    elif idade > maiorif and sexo in 'Ff':
        maiorif = idade
        femnv = nome
    if sexo in 'Ff':
        femtot += 1
    if sexo in 'Ff' and idade < 20:
        femi += 1
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    elif idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
print(f'Temos um total de {femtot} mulheres e {femi} delas são  menores de idade. \n '
      f'A mulher mais velha é a {femnv} com {maiorif} anos')
print(f'O homem mais velho é o {nomevelho} com {maioridadehomem} anos.')
print(f'A média de idade das pessoas é {midade / quantidade:.2f}')
