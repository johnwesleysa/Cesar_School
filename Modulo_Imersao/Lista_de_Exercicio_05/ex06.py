"""
Desenvolva um programa que permita aos usuários avaliarem restaurantes com notas de
0 a 5. Cada restaurante só deve ser inserido uma vez na lista. Se um restaurante for
avaliado mais de uma vez, o programa deve atualizar a nota média do restaurante
considerando todas as avaliações fornecidas até o momento, mas o restaurante não deve
ser adicionado novamente à lista.
O programa deve:
● Solicitar o nome do restaurante ou digitar “PARE” para finalizar. - OK
● Solicitar a nota dada pelo usuário (de 0 a 5). - OK
● Se o restaurante já foi avaliado anteriormente, atualizar a nota média
considerando todas as avaliações anteriores e a nova avaliação. Use a seguinte
fórmula: nova media = ((media anterior x numero de avaliações) + nova nota) / (numero de avaliações + 1)
"""
nome_restaurante = ""
lista_restaurantes = []
lista_notas = []
lista_medias_notas = []
cont_avaliacoes = 0


while nome_restaurante != "PARE":

    #Pega o nome do restaurante e se for pare ele encerra o loop
    nome_restaurante = input("Informe o nome do restaurante ou PARE para finalizar o programa: ")
    if nome_restaurante.upper() == "PARE":
        break

    #Armazena cada nome em uma posição do array, se o nome do restaurante não existe no array
    if nome_restaurante not in lista_restaurantes:
        lista_restaurantes.append(nome_restaurante)
        
        #Recebe uma nota de 0 a 5 do restaurante inserido
        nova_nota = int(input(f"Digite uma nota de 0 a 5: "))
        lista_notas.append(cont_avaliacoes + 1)
        lista_medias_notas.append(float(nova_nota))

    elif nome_restaurante in lista_restaurantes:
         #Recebe uma nota de 0 a 5 do restaurante inserido
        nova_nota = int(input(f"Digite uma nota de 0 a 5: "))

        #Pega o index do restaurante
        posicao_restaurante = lista_restaurantes.index(nome_restaurante)

        #Atualiza a quantidade de avaliações do restaurante
        lista_notas[posicao_restaurante] = lista_notas[posicao_restaurante] + 1

       #Pega a media anterior baseada no index do restaurante
        media_anterior = lista_medias_notas[posicao_restaurante]

        #Pega o numero de avaliações para o restaurante em questão baseadoo no index do restaurante
        numero_avalicoes = lista_notas[posicao_restaurante]

        #Calcula a nova media do restaurante
        #nova_media = ((media_anterior * numero_avalicoes) + nova_nota) / (numero_avalicoes + 1)
        nova_media = (media_anterior + nova_nota) / 2

        lista_medias_notas[posicao_restaurante] = nova_media


        
index_maior_nota = lista_medias_notas.index(max(lista_medias_notas))
index_menor_nota = lista_medias_notas.index(min(lista_medias_notas))

print(f"Restaurante com a maior nota: {lista_restaurantes[index_maior_nota]} - Nota média: {lista_medias_notas[index_maior_nota]}")
print(f"Restaurante com a menor nota: {lista_restaurantes[index_menor_nota]} - Nota média: {lista_medias_notas[index_menor_nota]}")