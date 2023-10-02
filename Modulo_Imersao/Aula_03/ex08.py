numeroInicial = int(input("Numero inicial: "))
numeroFinal = int(input("Numero final: "))
soma = 0

#utilizamos o +1 para usar o range exato informado
for i in range (numeroInicial, numeroFinal + 1):
    if i % 2 == 0:
        soma = soma + i
print(f"Soma dos numero pares no range informado: {soma}")