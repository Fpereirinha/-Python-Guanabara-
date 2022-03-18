'''salario = int(input('Qual o salário ??'))
cargo = int(input(Qual o cargo ?
[1] GERENTE
[2] OUTRO))
meses = int(input('Quantos meses trabalhados ?'))
x = 0
y = 0
z = 0
if cargo == 1 and meses > 12:
    x = 1.1
    y = 10
    z = .1
else:
    x = 1.05
    y = 5
    z = .05
if cargo != 1 and cargo != 2:
    print('Opção inválida.')
else:
    print(f'O aumento salarial será de {y}% e o novo salário é R${salario*x:.2f}\n '
          f'O respectivo aumento foi de R${salario*z:.2f}')'''
'''A = 10
B = 5
C = 2
x = True
y = False
if (B < A or C > B) and 2 * C < B or not x:
    print('real')
else:
    print('falso')
if C > A and A < C * 5:
    print('real')
else:
    print('falso')'''
'''soma = 0
quantidade = int(input('Qual a quantidade de números a serem somados ?'))
for c in range(1,quantidade +1):
    z = int(input(f'Digite o {c}° número a ser somado.'))
    soma += z
print(f'A soma de {quantidade} numeros é {soma}')'''
'''from random import randint
while True:
    x = randint(0, 100)
    if x == 100:
        print(x)
        break
    else:
        print(x)'''




