a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

semipetimetro = (a + b + c) / 2
raiz = (semipetimetro * (semipetimetro - a) * (semipetimetro - b) * (semipetimetro - c)) ** 0.5

print(f"Área do triângulo: {raiz}")