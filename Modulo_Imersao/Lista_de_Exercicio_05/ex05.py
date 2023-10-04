# Uma loja deseja avaliar o desempenho de seus vendedores. Crie um programa que:
# Solicite ao usuário o número total de vendedores da loja.
# Para cada vendedor, peça ao usuário o nome do vendedor e o total de vendas realizadas no ano.
# Determine o vendedor com o maior volume de vendas e o vendedor com o menor volume.
# Exiba o nome de todos os vendedores e suas vendas totais, destacando o vendedor com as vendas mais altas e o vendedor com as vendas mais baixas.

#Declaração de variáveis
nome_vendedor = []
total_vendas_anual = []

#Solicita o total de vendedores
total_vendedores_loja = int(input("Informe o número de vendedores da loja: "))


#Loop com o range de total de vendedores da loja
for i in range (total_vendedores_loja):
    #Solicita o nome do vendedor e armazena em uma lista
    nome_vendedor.append((input("Informe o nome do vendedor: ")))

    #Solicita o total de vendas anuais do mesmo vendedor e armazena em uma lista
    total_vendas_anual.append(int(input(f"Informe o total de vendas anual de {nome_vendedor[i]}: ")))


#Percorre um loop com o range de total de vendedores da loja
for i in range(total_vendedores_loja):
    #Se o numero total de vendas anual na posição i do array for igual ao maior número do array, imprime na tela o nome, total de vendas anual e um destaque de maior volume de vendas
    if total_vendas_anual[i] == max(total_vendas_anual):
        print(f"{nome_vendedor[i]}: {total_vendas_anual[i]} - Maior volume de vendas!")

    #Se o numero total de vendas anual na posição i do array for igual ao menor número do array, imprime na tela o nome, total de vendas anual e um destaque de menor volume de vendas
    elif total_vendas_anual[i] == min(total_vendas_anual):
        print(f"{nome_vendedor[i]}: {total_vendas_anual[i]} - Menor volume de vendas!")

    #imprime na tela o nome e total de vendas anual
    else: 
        print(f"{nome_vendedor[i]}: {total_vendas_anual[i]}")

        



