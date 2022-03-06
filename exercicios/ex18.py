from math import radians, tan, sin, cos

n = float(input('Qual o angulo para calcularmos seus valores?'))
print('O sen será {:.2f}. O Cos será {:.2f}. E a tg será {:.2f}.'.format(sin(radians(n)), cos(
    radians(
    n)),
                                                                         tan(radians(n))))
