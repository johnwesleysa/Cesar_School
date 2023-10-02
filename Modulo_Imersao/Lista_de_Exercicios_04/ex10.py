#Aluno: John Wesley Santos Alencar

num1 = int(input("Número 1:"))
num2 = int(input("Número 2:"))
print(num1)
print(num2)

soma = 0
penultimo_numero = num1
ultimo_numero = num2
prox_numero = ultimo_numero + penultimo_numero



for i in range(20):
    print(prox_numero)

    penultimo_numero = ultimo_numero
    ultimo_numero = prox_numero

    prox_numero = ultimo_numero + penultimo_numero

