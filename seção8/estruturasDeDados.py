# °-
'''
cidades = ['rio', 'sp', 'brasilia']
print(cidades[0])
cidades[0] = 'jequie'
print(cidades)
'''
# °-
'''
# funcoes dentro de uma lista
cidades.append('barra do choça')
print(cidades)
cidades.remove('jequie')
print(cidades)
cidades.pop(2)
cidades.insert(2, 'anage')
print(cidades)
cidades.sort()
print(cidades)
'''
# °-
'''
numeros = [0, 0, 0]
final = numeros*2
print(final)
letras = ['a', 'b', 'c']
final = numeros+letras
numeros.extend(letras)
print(final)
print(numeros)

intens = [['item1', 'item2'], 'item3']
print(intens[0][1])


nomes = ['creusa', 'creiton', 'atrobaldo', 'fulaninho']
aluno1, aluno2, aluno3, aluno4 = nomes
for aluno in enumerate(nomes, start=1):
    print(f'Aluno {i}: {aluno}')
'''
'''
nomes = ['creusa', 'creiton', 'atrobaldo', 'fulaninho']
aluno1, aluno2, *outros = nomes
print(aluno1)
print(aluno2)
print(outros)
'''

# °-LOOPING DENTRO DE UMA LISTA
'''
valores = [1, 2, 3, 4, 5, 6, 7, 8]
for x in valores:
    print(f'O valor ddo produto é R$ {x}')

nomes = ['creusa', 'creiton', 'atrobaldo', 'fulaninho']
aluno1, aluno2, aluno3, aluno4 = nomes
for i, aluno in enumerate(nomes, start=1):
    print(f'Aluno {i}: {aluno}')
'''
# °- VERIFICANDO ITENS EM UMA LISTA
'''
cor = ['amarelo', 'verde', 'rosa']
x = input('insira a cor desejada ')
if x.lower() in cor:
    print('temos essa cor')
else:
    print('nao temos essa cor')
'''
# °-AGREGANDO DUAS LISTAS COM O ZIP '''
# °- Input em uma lista
'''
frutas = input('dighite frutas separadas por virgula')
frutas_lista = frutas.split(', ')
print(frutas_lista)
'''

# °- Arrays
'''
from array import array
numeros = [1, 4, 6, 7, 90, 3, 4]
numeros_i = array('i', [1, 4, 6, 7, 90, 3, 4])
print(numeros_i)
'''
# °- SET'S
'''
list1 = [1, 2, 3, 5, 7, 9, 0]
list2 = [1, 2, 0, 4, 6, 8, 10]
num = set(list1)
nam = set(list2)
print(num | nam)
print(num-nam)
print(num ^ nam)
print(num & nam)
'''
# °-SET S COM STRINGS
'''
'''
# °- DICIONARIO
'''

'''
# °- FUNÇÃO LAMBDA
'''

#DEU ERRO NESSE CÓDIGO
def somar(x):
    def func2(x): return x+10
    return func2*4


print(somar(1))
'''
# °- FUNÇÃO MAP
'''
lista1 = [1, 2, 3, 4]
lista2 = []
for i in lista1:
    i *= 2
    lista2.append(i)
print(lista2)

lista1 = [1, 2, 3, 4]


def mul(x):
    return x*2


lista2 = map(mul, lista1)
'''
# °- MAP COM LAMBDA
'''
lista1 = [1, 2, 3, 4]
print(list(map(lambda x: x*2, lista1)))
'''
# °-FUNÇÃO FILTER
'''
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]



print(list(filter(lambda x: x > 5, valores)))
'''

# °- LIST COMPREHENSION
'''
frutas = ['abacate', 'morango', 'uva', 'maça', 'banana']
frutas2 = []
for comida in frutas:
    if 'n' in comida:
        frutas2.append(comida)
print(frutas2)

frutas = ['abacate', 'morango', 'uva', 'maça', 'banana']
frutas2 = [iten for iten in frutas if 'o' in iten]
print(frutas2)
'''
# # °- LIST COMPREHENCION COM NUMEROS
'''
# valores = []
# for x in range(1, 6):
#     valores.append(x*10)
valores = [x*10 for x in range(1, 6)]
print(valores)
'''

# °- LISTA E GENERATOR EXPRESSIONS'''
from sys import getsizeof
valores = [x*10 for x in range(1, 1000)]
print(type(valores))
print(getsizeof(valores))
print('---------')
valores = (x*10 for x in range(1, 1000))
print(type(valores))
print(getsizeof(valores))
# °- '''
# °- '''
# °- '''
# °- '''
# °- '''
# °- '''
# °- '''
# °- '''
