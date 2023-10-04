notas = []

for i in range(5):
    notas.append(float(input(f"Digite a nota {i}: ")))
    
media = sum(notas) / len(notas)

for i in notas:
    if i > media:
        print(f"{i}")