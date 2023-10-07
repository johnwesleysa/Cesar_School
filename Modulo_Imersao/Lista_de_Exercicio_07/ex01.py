"""Crie um programa que contenha uma lista de tuplas, onde cada tupla contém o
nome de uma cor e seus valores RGB (Red, Green, Blue), informadas pelo
usuário. Para inserir os valores, o sistema deverá solicitar quantas cores o
usuário deseja informar. Após a inserção, solicite ao usuário que digite o nome
de uma cor e, se a cor estiver na lista, exiba seus valores RGB."""

qtd_cores = int(input("Informe quantas cores você deseja adicionar: "))
cores = []

for i in range(qtd_cores):
    nome_cor = input("Qual o nome da cor? ")
    r = int(input("Valor Red: "))
    g = int(input("Valor Green: :"))
    b = int(input("Valor Blue: "))

    cores.append((nome_cor, r, g, b))

cor_desejada = input("Qual cor você deseja encontrar? ")

for cor in cores:
    if cor[0] == cor_desejada:
        cor_encontrada = cor
        break

if cor_encontrada:
    print(f"Valores RGB para a cor {cor_desejada}: Red={cor_encontrada[1]}, Green={cor_encontrada[2]}, Blue={cor_encontrada[3]}")
else:
    print(f"A cor {cor_desejada} não foi encontrada: ")
