numeros_maria = {'a': 100, 'b': 200, 'c': 300}
numeros_sara = {'a': 300, 'b': 200, 'd': 400, 'c': 500, 'e': 250}

for letra in numeros_maria:
    if letra in numeros_sara:
        numeros_maria[letra] = numeros_sara[letra]
    else: break

print(f"Os valores do dicionário numeros_maria são: {numeros_maria}")
    