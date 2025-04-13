genero = int(input("digite seu genero 1- para homem 2- para mulher: "))
altura = float(input("digite sua altura em metros: "))
if genero == 1:
    print((72.7 * altura) - 58)
else:
    print((62.1 * altura) - 44.7)