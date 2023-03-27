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


def somar(a, b):
    s = a + b
    return s


def leiaint(msg):
    try:
        numero = int(input(msg))
    except (TypeError, ValueError):
        print(f'{cores["vermelho"]}Erro!{cores["limpar"]} digite um número valido.')
    else:
        return numero