dias_pares = ([],[])
dias_impares = ([],[])


for i in range(5):
    nome_enfermeiro = input("Digite o nome do enfermeiro: ")
    while True:
        dia_trabalhado = int(input("Digite um número de 1 a 30 para o dia trabalhado: "))
        if dia_trabalhado >= 1 and dia_trabalhado <= 30:
            if dia_trabalhado % 2 == 0:
                dias_pares[0].append(nome_enfermeiro)
                dias_pares[1].append(dia_trabalhado)
            else:
                dias_impares[0].append(nome_enfermeiro)
                dias_impares[1].append(dia_trabalhado)
            break
        else:
            print("Dia inválido! Digite um dia entre 1 e 30")
            continue
    
print(f"Pessoas no plantão (dias pares): {dias_pares}")
print(f"Pessoas no plantão (dias ímpares): {dias_impares}")