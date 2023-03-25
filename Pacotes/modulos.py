cores = {"azul": '\033[34m',
         "vermelho": '\033[31m',
         "amarelo": '\033[33m',
         "verde": '\033[32m',
         "roxo": '\033[35m',
         "limpar": '\033[m'}


def line(msg):
    print(f'{cores["roxo"]}-{cores["limpar"]}' * len(msg))
    print(f'{cores["verde"]}{msg}{cores["limpar"]}')
    print(f'{cores["roxo"]}-{cores["limpar"]}' * len(msg))