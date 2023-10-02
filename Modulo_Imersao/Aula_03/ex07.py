notas = 0.0
qtdNotas = 0
media = 0.0
soma = 0.0
while notas != 1:
    notas = float(input("Digite sua nota ou -1 para sair: "))
    if notas == -1:
        break
    qtdNotas += 1
    soma = soma + notas
media = soma / qtdNotas
print(f"Quantidad de notas informa foi {qtdNotas} e a media foi {media}")
    