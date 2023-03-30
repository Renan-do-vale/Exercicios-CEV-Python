from Pacotes.modulos import dobro,leiaint,cores,triplo,quadrado

num = leiaint('Digite um número: ')
print(f'O dobro de {num} é {cores["verde"]}{dobro(num)}{cores["limpar"]}')
print(f'O triplo de {num} é {cores["verde"]}{triplo(num)}{cores["limpar"]}')
print(f'Raide quadrada de {num} é {cores["verde"]}{quadrado(num):.1f5}{cores["limpar"]}')