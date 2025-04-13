import math
cx1 = float(input("Digite a coordenada x1: "))
cy1 = float(input("Digite a coordenada y1: "))
cx2 = float(input("Digite a coordenada x2: "))
cy2 = float(input("Digite a coordenada y2: "))

distancia = math.sqrt((cx2 - cx1) ** 2 + (cy2 - cy1) ** 2)
print(f"a distancia entre estes dois ponto e de:{distancia}")
