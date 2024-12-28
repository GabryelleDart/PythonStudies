# Aula de Criação de objetos
'''
# classes- agrupam dados e funções podendo reutilizar
# . significa metodo
class Funcionarios:
    # pass significa classe vazia
    pass
#criação de objeto        
usuario1=Funcionarios()
#crio parametros do user 1
usuario1.nome='Gaby'
usuario1.sobrenome='Duarte'
usuario1.data_nascimento='20/01/2004'
'''
# Aula de construtores
from datetime import datetime


class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def ano(self):
        ano_atual = int(datetime.now().year)
        anoy = int(self.data_nascimento[-4:])
        return ano_atual - anoy


user1 = Funcionarios('GABY', 'DUARTE', '20/01/2004')
user2 = Funcionarios('CLAUDIO', 'DUARTE', '11/10/1989')
print(user1.nome_completo())
print(user1.ano())
