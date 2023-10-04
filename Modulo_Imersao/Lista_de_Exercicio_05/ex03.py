#Faça um programa em duas partes:
#○ Parte 01: Ler 10 números inteiros e armazená-los em uma lista única.
#○ Parte 02: Em uma nova estrutura de repetição, armazene os números pares na
#lista PARES e os números ímpares na #lista ÍMPARES.
#○ Imprima as três listas.


numeros_inteiros = []
pares = []
impares = []

#PARTE 1 - : Ler 10 números inteiros e armazená-los em uma lista única.

for i in range(10):
    numeros_inteiros.append(int(input("Digite um número inteiro: ")))

#PARTE 2 - Em uma nova estrutura de repetição, armazene os números pares na lista PARES e os números ímpares na lista ÍMPARES.


for i in numeros_inteiros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Números: {numeros_inteiros}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

