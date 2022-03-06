import time

n = int(input('Me diga um número e te direi se é impar ou par'))
r = n % 2
print('Estou calculando, um momento.')
print('-=' * 20)
time.sleep(2)

if r == 0:
    print('O número é par.')
else:
    print('O resultado é impar !')
