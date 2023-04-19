from Pacotes.modulos import leiafloat, calcDesconto, leiaint

precoProduto = leiafloat('Qual é o preço do produto? R$')
desconto = leiaint('Qual o desconto em %: ')
print(f'o produto que custava R${precoProduto} com desconto de {desconto:.0f}% va custar R${calcDesconto(precoProduto, desconto):.2f}')