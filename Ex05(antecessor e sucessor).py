from Pacotes.modulos import leiaint,cores
from time import sleep
n = leiaint('Digite um número: ')
print(f'{cores["verde"]}Analisando o valor {n}...{cores["limpar"]}')
sleep(1)
print(f'O antecessor de {n} é {cores["roxo"]}{n-1}{cores["limpar"]} e o sucessor é {cores["roxo"]}{n+1}{cores["limpar"]}')