#Aluno: John Wesley Santos Alencar

maiorNumPar = 0
numPar = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))

    if num % 2 == 0:
        if num > maiorNumPar:
            maiorNumPar = num


print(f"Maior número par: {maiorNumPar}")