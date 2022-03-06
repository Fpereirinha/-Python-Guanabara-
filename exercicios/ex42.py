l1 = float(input('Qual o primeiro segmento ?'))
l2 = float(input('Qual o segundo segmento ?'))
l3 = float(input('Qual o terceiro segmento ?'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Os segmentos são capazes de formarem um triangulo.')
    if l1 == l2 == l3:
        print('E ele é classificado como EQUILATERO.')
    elif l1 != l2 != l3 != l1:
        print('E ele é um triangulo ESCALENO.')
    else:
        print('E ele é um triangulo ISOCELES')
else:
    print('Os segmentos não são capazes de formarem um triangulo.')
