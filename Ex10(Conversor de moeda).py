from Pacotes.modulos import leiafloat,ConversorDolar
r = leiafloat('How much money do you have in your wallet? R$')
print(f'With R${r:.2f} you can buy US${ConversorDolar(r):.2f}')