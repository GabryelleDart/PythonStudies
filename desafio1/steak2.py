# uso no range , range é lista de numeros
try:
    temp = int(input('Qual a temperatura da carne em Celsius?\n'))
except ValueError:
    print("Entrada inválida")
else:
    if temp < 48:
        print('mataram a vaca a toa')
    elif temp in range(48, 54):
        print("A carne está selada")
    elif temp in range(54, 60):
        print("A carne está ao ponto para mal")
    elif temp in range(60, 65):
        print("A carne está ao ponto")
    elif temp in range(65, 71):
        print("A carne está ao ponto para bem")
    else:
        print("A carne está bem passada")
