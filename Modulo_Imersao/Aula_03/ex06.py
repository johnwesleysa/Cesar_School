idade = 0
i = 0
while idade != -1:
    idade = int(input("Idade:"))
    if idade < 18:
        continue
    i += 1
print(f"Idade maiores ou iguais a 18: {i}")