'''t = int(input('Qual será o primeiro termo da PA?'))
r = int(input('Qual é a razão?'))
for c in range(t,(10*r)+t,r):
    print(c, end= ' ')'''
t = int(input('Qual o primeiro termo da PA ?'))
r = int(input('Qual a razão da PA?'))
c = 0
'''while c < 10:
    if c == 0:
        print(t)
    else:
        print(t + (r * c))
    c += 1'''
while c < 10:
    print(t)
    c += 1
    t += r
str = input()