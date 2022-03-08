maior = homem = mulher = 0
while True:
    idade = int(input("Qual a idade ?"))
    sexo = str(input("Sexo: [M/F]")).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F]")).upper().strip()[0]
    if sexo == 'F' and idade < 20:
        mulher += 1
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    Choice = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
    while Choice not in 'SN':
        Choice = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
    if Choice == 'N':
        break
print(f'Temos um total de {maior} maiores de 18 anos\nAo todo temos {homem} homens cadastrados. \n'
      f'E temos {mulher} mulheres com menos de 20 anos.')





