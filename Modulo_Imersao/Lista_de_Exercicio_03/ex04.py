#Em uma cidade, a prefeitura deseja classificar os motoristas com base 
#em suas infrações de trânsito no último ano. O objetivo é criar um 
#programa de reeducação para os motoristas que cometem infrações. Para 
#isso, eles definiram as seguintes categorias:
#a) Motorista Exemplar: Não cometeu nenhuma infração.
#b) Motorista Atento: Cometeu até 3 infrações.
#c) Motorista Desatento: Cometeu entre 4 e 6 infrações.
#d) Motorista Perigoso: Cometeu mais de 6 infrações.
#Escreva um programa que peça ao usuário para inserir o número de #infrações que cometeu no último ano e informe em qual categoria ele se 
#encaixa.

infracoes = int(input("Número de infrações do último ano: "))

if infracoes == 0:
    print("Motorista Exemplar")
elif 1 <= infracoes <= 3:
    print ("Motorista Atento")
elif 4 <= infracoes <= 6:
    print("Motorista Desatento")
elif infracoes > 6:
    print("Motorista Perigoso")
else: 
    print("Opção inválida!")