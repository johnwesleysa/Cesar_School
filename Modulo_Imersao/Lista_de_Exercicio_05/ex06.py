"""

Desenvolva um programa que permita aos usuários avaliarem restaurantes com notas de
0 a 5. Cada restaurante só deve ser inserido uma vez na lista. Se um restaurante for
avaliado mais de uma vez, o programa deve atualizar a nota média do restaurante
considerando todas as avaliações fornecidas até o momento, mas o restaurante não deve
ser adicionado novamente à lista.
O programa deve:
● Solicitar o nome do restaurante ou digitar “PARE” para finalizar.
● Solicitar a nota dada pelo usuário (de 0 a 5).
● Se o restaurante já foi avaliado anteriormente, atualizar a nota média
considerando todas as avaliações anteriores e a nova avaliação. Use a seguinte
fórmula: nova media = ((media anterior x numero de avaliações) + nova nota) / (numero de avaliações + 1)

"""
nome_restaurante = ""
nomes_restaurantes = []
notas_medias = []
contagem_avaliacoes = []

while nome_restaurante != "PARE":
    nome_restaurante = input("Informe o nome do restaurante ou PARE para finalizar o programa: ")
    if nome_restaurante.upper == "PARE":
        

