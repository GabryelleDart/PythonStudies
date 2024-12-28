# Funções
'''
def boas_vindas():
    print("Ola Gaby.\nTemos 5 laptops em estoque.")
'''
# Funções de soma
'''
x = int(input('Insira um numero'))
y = int(input('Insira outra numero'))

somar(x,y)


def somar (x,y):
    print(f'O resultado da soma é {x+y}')
    
a função tem que ficar em cima do codigo

def somar(x, y):
    print(f'O resultado da soma é {x+y}')


x = int(input('Insira um numero'))
y = int(input('Insira outra numero'))

somar(x, y)

'''
# Parametros e argumentos'
'''


def boas_vindas(nome):
    print(f'Ola {nome}.\nTemos 5 laptops em estoque.')


nome = input('Digite seu nome')
boas_vindas(nome)
'''

# Argumentosdefault ou não'''
# Argumentosdefault xargs com numeros
'''


def soma(*numbers):
    s = 0
    for num in numbers:
        s += num
    return s


x = soma(1, 2, 3, 4, 5)
print(x)
'''
# argumentos xargs nomeando parametros
'''

def carro(*details):
    return details[1]


print(carro("HB20", 'BRANCO', '2028'))



def carro(**details):
    return details


# arfumentos significam que eu posso passar abaixo os meus parametros
print(carro(modelo="HB20", cor='BRANCO', ano='2028'))
'''
# Importando um módulo
# tentando fazer o código de fatorial e deu errado
'''

def fat(y):
    i = int(1)
    for num in y(1, (y+1)):
        i *= num
    return i


print(fat(x=int(input('Digite o numero'))))

# fatorial com biblioteca
import math
print(math.factorial(3))
'''