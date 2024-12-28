# 1° código
'''print("hello world")
'''

# 2° código
'''x = "oioioio"
print(x)
'''

# 3° código
'''
x = str(9)
y = int(12)
z = float(3)
print(x+3) #deveria dar 93 , mas o vscode n permite 
print(y+3)
print(z+3)
'''

# 4° código
'''
nome = 'andre'
idade = str(32) #n consegue concaternar string e int. 
cidade = 'São paulo'
print('O '+nome+'tem' + idade+'anos. E mora'+cidade)
'''

# 5° código
'''
nome = 'andre'
idade = 32  # n consegue concaternar string e int.
idade = str(idade)
cidade = 'São paulo'
print('O '+nome+' tem ' + idade+' anos. E mora em '+cidade)
'''

# 6° código
'''nome = 'andre'
idade = 32  # n consegue concaternar string e int.
cidade = 'São paulo'
print('O '+nome+' tem ' + str(idade)+' anos. E mora em '+cidade)
'''

# 7° código
'''nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')
cidade = input('Onde vc mora?')
print('O '+nome+' tem ' + idade+' anos. E mora em '+cidade)
'''

# 8° código
'''
#para saber o tipo de dado que o input ta recendo coloque print(print(variavel))
#em input ele entra com uma string
ano = input('em que ano vc nasceu?')
id = 2024-int(ano)
print("Vc tem "+str(id) + " anos")
'''

# 9° código
''' 
#SLICE- pegar apenas fragmentos de uma variavel
fruta = "manga"
print(fruta[2])
frase = "o rato roeu a roupa do rei de roma"
# colocar um a mais no final pq o index so pega o final - 1 , se vc quer ate o 10 coloque 11
print(frase[0:11])
numero = 77.99
numero = str(numero)
print(nmero[2:5])
'''
# 10° código
'''
# como imprimir strings formatadas
nome = 'marcos'
sobrenome = 'silva'
profissão = 'programador'

texto = f'O {nome} {sobrenome} é um otimo [{profissão}] .'
print(texto)
'''
mensagem = 'Gaby ama o Cláudio'
print(mensagem.replace(' o ', ' a bunda do '))
