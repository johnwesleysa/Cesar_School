
nomes = []
idades = []

for i in range(18):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    if idade >= 18:
       nomes.append(nome)
       idades.append(idade)

tupla_pessoas = (nomes, idades)
print(tupla_pessoas)
