from Pacotes.modulos import leiafloat, leiaint, calcAumento

salario = leiafloat('Qual é o salário do funcionário? R$')
aumento = leiaint('Qual o aumento em % ')
print(f'Um funcionário que ganhava {salario:.2f}, com {aumento}% de aumento, passa a receber R${calcAumento(salario,aumento):.2f}')