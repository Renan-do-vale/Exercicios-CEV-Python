from Pacotes.modulos import leiaint,somar,cores

n1 = leiaint('Digite um número:')
n2 = leiaint('Digite outro número: ')
print(f'  {cores["azul"]}{n1} + {n2}{cores["limpar"]} = {cores["verde"]}{somar(n1,n2)}{cores["limpar"]}.')