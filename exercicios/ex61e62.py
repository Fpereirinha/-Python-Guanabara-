'''t = int(input('Qual será o primeiro termo da PA?'))
r = int(input('Qual é a razão?'))
for c in range(t,(10*r)+t,r):
    print(c, end= ' ')'''
t = int(input('Qual o primeiro termo da PA ?'))
r = int(input('Qual a razão da PA?'))
c = 0
x = 10
total = 0
'''while c < 10:
    if c == 0:
        print(t)
    else:
        print(t + (r * c))
    c += 1'''
while x != 0:
    total += x
    while c < total:

        print(t)
        c += 1
        t += r
    print('pausa')
    x = int(input('Quantos termos a mais ?'))

print('FIM total de {} números'.format(c,))

