#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário como
#String. Usando manipulação de Strings, altere a frase e exiba como no exemplo.


meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Setembro', 'Novembro', 'Dezembro']

data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
split_data = data_nasc.split()
print(split_data)
index_mes = (split_data[2]) - 1

frase_saida = f"Você nasceu em {split_data[0]} de {meses_ano[index_mes]} de {split_data[4]}"

