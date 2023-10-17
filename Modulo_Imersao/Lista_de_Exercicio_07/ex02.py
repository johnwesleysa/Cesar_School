import math

def distancia_entre_pontos(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    calc = round(math.sqrt(dx**2 + dy**2 + dz**2), 2)
    return calc


x1 = float(input("x1: "))
x2 = float(input("x2: "))
y1 = float(input("y1: "))
z2 = float(input("y2: "))
y2 = float(input("z1: "))
z1 = float(input("z2: "))
p1 = (x1, y1, z1)
p2 = (x2, y2, z2)
distancia = distancia_entre_pontos(p1, p2)
print(f"A distância entre os pontos é {distancia}")
