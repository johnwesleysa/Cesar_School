maiorAltura = 0
nomeMaiorAltura = ""
idadeMaiorAltura = 0

for i in range(5):
    nome = input("Digite sem nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    if i == 0:
        nomeMaiorAltura = nome
        idadeMaiorAltura = idade
        maiorAltura = altura
    elif altura > maiorAltura:
        nomeMaiorAltura = nome
        idadeMaiorAltura = idade
        maiorAltura = altura

print(f"{nomeMaiorAltura}, com {idadeMaiorAltura} anos e {maiorAltura}m, é a pessoa mais alta do grupo.")
        