"""
Crie um programa que leia as coordenadas x, y e z de dois pontos no espaço 3D,
representados como tuplas. Calcule a distância entre esses dois pontos usando a
fórmula da distância Euclidiana:

"""
import math
x1 = (1.0)
x2 = (2.0)
y1 = (3.0)
y2 = (4.0)
z1 = (5.0)
z2 = (6.0)

d = round(math.sqrt((((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2))))
print(d)
