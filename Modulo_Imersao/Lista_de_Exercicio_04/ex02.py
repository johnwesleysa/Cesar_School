#Aluno: John Wesley Santos Alencar

nota = 0
soma = 0
media = 0.0
qtdNotas = 0

while nota != -1:
    nota = int(input("Digite uma nota de 1 a 5 ou -1 para sair: "))

    if nota < 1 or nota > 5 and nota != -1:
        print("Nota inválida!")
        continue
    
    qtdNotas += 1
    soma = soma + nota

media = soma / qtdNotas

print(f"Média das notas: {media}")
    