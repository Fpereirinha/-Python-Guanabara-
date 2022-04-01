# esse exercicio requer os modulos de números.
from Modulos.Numeros import metade, dobro, aumento, diminui, moedares, moeda

x = float(input('Digite o preço:'))
print(f'A metade de {x} é R${metade(x):.2f}'
      f'\nO dobro de {x} é R${dobro(x):.2f}'
      f'\nAumentando 10% temos R${aumento(x, 10):.2f}'
      f'\nDiminuindo 10% temos R${diminui(x, 10):.2f}'.replace('.', ','))
# caso necessario poderiamos usar outras funções como moeda para formatação
# moeda(Valor)
# print(moeda(aumento(1000, 2)))
moedares(10000, 200, 70)
