from Pacotes.modulos import leiaint

diasAlugados = leiaint('Quantos dias alugados? ')
KmRodados = leiaint('Quantos Km rodados? ')

def TotalPagar(dias, km):
    pagar = (dias * 60) + (km * 0.15)
    return pagar

print(f'O total a pagar é de R${TotalPagar(diasAlugados,KmRodados):.2f}')