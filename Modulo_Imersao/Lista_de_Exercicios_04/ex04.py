qtdBanho = 0
qtdTosa = 0
qtdBanho_Tosa = 0
qtdOutros = 0


for i in range (10):
    codigo_servico = int(input("Digite o código do serviço 1 - banho; 2 - tosa; 3 - banho e tosa; 4 - outros: "))

    if codigo_servico == 1:
        qtdBanho += 1
    elif codigo_servico == 2:
        qtdTosa += 1
    elif codigo_servico == 3:
        qtdBanho_Tosa += 1
    elif codigo_servico == 4:
        qtdOutros += 1

print(f"Banho : {qtdBanho}")
print(f"Tosa : {qtdTosa}")
print(f"Banho e tosa : {qtdBanho_Tosa}")
print(f"Outros : {qtdOutros}")