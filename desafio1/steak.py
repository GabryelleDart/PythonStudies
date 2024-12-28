try:
    temp = int(input('Qual a temperatura da carne em Celsius?\n'))
except ValueError:
    print("Entrada inválida")
else:
    if (48 <= temp < 54):
        print("A carne está crua")
    elif (54 <= temp < 60):
        print("A carne está ao ponto para mal passada")
    elif (60 <= temp < 65):
        print("A carne está ao ponto ")
    elif (65 <= temp < 71):
        print("A carne está ao ponto para bem passada")
    elif (temp > 71):
        print("A carne está bem passada")
    else:
        print("mataram a vaca para nada")
