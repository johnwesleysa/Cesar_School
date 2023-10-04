#Faça um programa que leia um número indeterminado de valores, 
#correspondentes a
#idades, encerrando a entrada de dados quando for informado um 
#valor igual a -1 (que
#não deve ser armazenado). Após esta entrada de dados, faça:
#○ Mostre a quantidade de idades válidas;
#○ Exiba as idades armazenadas;
#○ Calcule e mostre a média das idades;
#○ Calcule e mostre a quantidade de idades acima da média #calculada;
#○ Exiba a maior e menor idade;
#○ Calcule e mostre a quantidade de valores abaixo de 18.

#Declaração de variáveis
idade = 0
lista_idades = []
media_idades = 0.0
qtd_idades_acima_da_media = []
qtd_menor_dezoito = []

#Enquanto idade for diferente de -1 o programa irá solicitar uma nova idade
while idade != -1:
    idade = int(input("Idade: "))
    if idade == -1:
        break

    #Se idade for válida armazena no array idade.
    if idade > 0:
        lista_idades.append(idade)

#Calcula a média das idades 
media_idades = sum(lista_idades) / len(lista_idades)

#Percorre o array lista_idades
for i in lista_idades:

    #Se idade for maior que a media de idades, armazena essa idade em um novo array.
    if i > media_idades:
        qtd_idades_acima_da_media.append(i)
    
    #Se idade maior que 18 armazena essa idade em um novo array
    if i < 18:
        qtd_menor_dezoito.append(i)

print(f"Quantidade de idades válidas: {len(lista_idades)}")
print(f"Idades armazenadas: {lista_idades}")
print(f"Média das idades: {media_idades}")
print(f"Quant. de idades acima da média: {len(qtd_idades_acima_da_media)}")
print(f"Maior idade: {max(lista_idades)}")
print(f"Menor idade: {min(lista_idades)}")
print(f"Quant. de idades abaixo de 18: {len(qtd_menor_dezoito)}")






