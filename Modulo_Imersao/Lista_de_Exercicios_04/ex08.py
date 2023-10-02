soma_desconto = 0.0
qtd_aptos_desconto = 0


quantos_clientes = int(input("Quantos clientes há na loja? "))

for i in range(quantos_clientes):
    nome = input("Digite seu nome: ")
    valor_compras_anual = float(input("Valor total das compras no ano: "))

    if valor_compras_anual >= 2000:
        print("Cliente apto para receber o bônus")

        desconto = valor_compras_anual * 0.15
        soma_desconto = soma_desconto + desconto
        qtd_aptos_desconto += 1

print(f"Clientes: {qtd_aptos_desconto}")
print(f"Total: R$ {soma_desconto}")