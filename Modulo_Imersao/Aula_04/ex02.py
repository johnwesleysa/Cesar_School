numero = []

for i in range(10):
    numero.append(int(input("Digite um número: ")))

print(f"{numero}")
print(f"Menor valor da lista: {min(numero)}")

numeroMaior = 0
numeroImpar = 0
numeroIndice = 0
if i in range(len(numero)):
    if i == 0:
        numeroMaior = numero[i]
        numeroIndice = i
    elif numero[i] > numeroMaior:
        numeroMaior = numero[i]
        numeroIndice = i

    if numero[i] % 2 == 0:
        numeroImpar +=1

print(f"Maior Número é {numeroMaior} e seu indice é {numeroIndice}")
print(f"Numero impares {numeroImpar}")
