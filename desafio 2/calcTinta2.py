import math
l = (int(input('Qual a largura da parede?\n')))
h = (int(input('Qual a altura da parede ?\n')))
r = (int(input('Qual o rendimento da lata de tinta comprada? \n')))


def calc(l, h, r):
    if ((l*h) % r == 0):
        return str((l*h) % r)
    else:
        return str(math.floor((l*h)/r)+1)


print("Você precisa de " + calc(l, h, r) + " latas de tinta.")
