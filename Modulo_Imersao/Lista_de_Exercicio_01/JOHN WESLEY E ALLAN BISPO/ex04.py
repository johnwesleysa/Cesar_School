valor = float(input("Valor inicial: "))
juros = float(input("Taxa de juros: "))
tempo = int(input("Tempo: "))

calc = (valor * (juros / 100) * tempo) + valor

print(f"Valor futuro: {calc}")