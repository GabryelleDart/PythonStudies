# 1°-operadores logicos
'''
rendamais5mil = False
nomelimpo = True
if rendamais5mil or nomelimpo:
    print("pode comprar um carro")
else:
    print("não pode comprar um carro")
'''
# 2°-multiplos operadores de comparação
'''
valor = 20
if valor >= 20 and valor < 40:
if 20<=valor <40:
    #ambas as operações resultam na mesma coisa
    print("aceito")
else:
    print("bao aceito")
'''
# 4° for loops
'''
for a in range(4):
    print(a)


for n in range(1, 6):
    print(n)



for b in range(7, 12, 2):
    print(b)
'''
# 4° for loops
'''
for vogals in 'Google':
    print(vogals)

site = 'apple'
i = 0
for letra in site:
    print(f'{letra} esta na posição {i+1} da palavra {site}')
    i += 1
'''
# 5° for loops com if else
'''

compraComfirmadas = False
dadosCompra = 'compra no valor de 150 reais e detalhes enviados para o seu email'
# envio foi uma variavel aleatoruo pois nao seri possivel colocar a comprasconfirmadas pois ele iria apenas percorrer a variavel
for envio in range(3):
    if compraComfirmadas:
        print(dadosCompra)
        print('Detalhes encaminhados para o email')
        break
    else:
        print('Falha na compra')
        '''
# 6° loops dentro de outros loops - nested loops
'''
for n1 in range(10):
    print("Produto" + str(n1))
    for n2 in range(1, 3):
        print(n1, n2)
'''
# 7° separando strings
'''
palavra = 'FANTA'
for letra in palavra:
    print(letra, end=' ')


palavra = 'FANTA'
for letra in palavra:
    print(f'{letra}', end=' ')
'''
# 8°
# criar um retangulo feito de simbolos
'''
y = int(input("insira o numero de colunas"))
x = int(input("insira o numero de linhas"))

for c in range(y):
    for l in range(x):
        print('@', end='')
    print()
    '''
# 9° While loop
'''
valor = 100
i = 1
while valor > 20:
    print(f'Fulaninha comprou o produto no dia. {i} Pagou R$ {
          valor}.Ganhou um desconto de {100-valor}%.')
    i += 1
    valor -= 5
    '''
# 10° Operador ternario
'''
id = 16
resultado = "permitido" if id >= 16 else "naõ permitido"
print(resultado)'''
# 11° Operaçoes com while '''
valor = int(input('Digite o valor do produto: '))
while valor > 20:
    print(f' O valor do produto ficará {valor*1.1} com a  comissão ')
    break
