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
contador = 0
media_anterior = 0.0
nova_media = 0.0
media_atual = 0.0
cont = 0


while nome_restaurante != "PARE":

    #Pega o nome do restaurante e se for pare ele encerra o loop
    nome_restaurante = input("Informe o nome do restaurante ou PARE para finalizar o programa: ")
    if nome_restaurante.upper() == "PARE":
        break

    #Armazena cada nome em uma posição do array, se o nome do restaurante não existe no array
    if nome_restaurante not in lista_restaurantes:
        lista_restaurantes.append(nome_restaurante)

        #Recebe uma nota de 0 a 5 do restaurante inserido
        nota = int(input(f"Digite uma nota de 0 a 5: "))
        lista_notas.append(nota)
        lista_medias_notas.append(nota)

    elif nome_restaurante in lista_restaurantes:
        posicao_restaurante = lista_restaurantes.index(nome_restaurante)
        media_anterior = lista_medias_notas[posicao_restaurante]
        media_atual = media_anterior * (₢)

    
    
    


    

    
    contador += 1

    
print(lista_notas)
print(lista_restaurantes)

    




    




        

