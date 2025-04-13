lado1 = int(input("digite o comprimento do lado1:"))
lado2 = int(input("digite o comprimento do lado2:"))
lado3 = int(input("digite o comprimento do lado3:"))
if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    if lado1 == lado2 and lado1 == lado3:
        print("triangulo equilatero")
    else: 
        print("triangulo isoseles")
else:
    print("triangulo escaleno")               
