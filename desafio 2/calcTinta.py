import math
l = (int(input('Qual a largura da parede?\n')))
h = (int(input('Qual a altura da parede ?\n')))
r = (int(input('Qual o rendimento da lata de tinta comprada? \n')))
print("Você precisa de " + str(math.ceil((l*h)/r)) + " latas de tinta.")
