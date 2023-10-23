"""
Crie um programa que leia as coordenadas x, y e z de dois pontos no espaço 3D,
representados como tuplas. Calcule a distância entre esses dois pontos usando a
fórmula da distância Euclidiana:

"""
import math
x = (1.0, 2.0)
y = (3.0, 4.0)
z = (5.0, 6.0)

subX = x[0] - x[1]
subY = y[0] - y[1]
subZ = z[0] - z[1]

d = math.sqrt((subX ** 2) + (subY**2) + (subZ  ** 2))

print(d)

