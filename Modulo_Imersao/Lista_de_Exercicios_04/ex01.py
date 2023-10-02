idade = 0
somaIdade = 0
qtdMaiorVinteCinco = 0
qtdMenorVinteCinco= 0
media = 0.0
qtdIdade = 0

while idade != -1:
    idade = int(input("Idade: "))

    if idade == -1:
        break
    qtdIdade += 1
    somaIdade = somaIdade + idade

    if idade > 25:
        qtdMaiorVinteCinco += 1
    else:
        qtdMenorVinteCinco += 1

media = somaIdade / qtdIdade

print(f"Total de idades: {qtdIdade}")
print(f"Média das idades: {media}")
print(f"Maiores de 25 anos: {qtdMaiorVinteCinco}")
print(f"Menores de 25 anos: {qtdMenorVinteCinco}")


