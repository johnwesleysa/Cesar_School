menorIdade = 0
maiorIdade = 0

for i in range (5):
    idade = int(input("Digite idade: "))
    if i == 0:
        menorIdade = idade
        maiorIdade = idade
    elif idade < menorIdade:
        menorIdade = idade
    elif idade > maiorIdade:
        maiorIdade = idade
print(f"Menor idade é {menorIdade}")
print(f"Maior idade é {maiorIdade}")
    