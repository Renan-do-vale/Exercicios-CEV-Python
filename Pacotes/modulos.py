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
    while True:
        try:
            numero = int(input(msg))
        except (TypeError, ValueError):
            print(f'{cores["vermelho"]}Erro!{cores["limpar"]} digite um número valido.')
        else:
            return numero
            break
    

def scanv(n):
    print(f'Tipo da variavel é {cores["roxo"]}{type(n)}{cores["limpar"]}')
    print(f'É Alfanúmerico? {cores["roxo"]}{n.isalnum()}{cores["limpar"]}')
    print(f'É númerico? {cores["roxo"]}{n.isnumeric()}{cores["limpar"]}')
    print(f'É Alfabeto? {cores["roxo"]}{n.isalpha()}{cores["limpar"]}')
    print(f'Pode imprimir? {cores["roxo"]}{n.isprintable()}{cores["limpar"]}')
    print(f'Só tem espaços? {cores["roxo"]}{n.isspace()}{cores["limpar"]}')


def dobro(n):
    r = 2 * n
    return r


def triplo(n):
    r = 3 * n
    return r


def quadrado(n):
    r = n ** (1/2)
    return r