#Escreva um algoritmo que receba o código correspondente ao cargo de um 
#funcionário de uma escola e seu salário atual. Mostre o valor do novo 
#salário, com aumento, conforme tabela abaixo:

codigoCargo = int(input("Digite seu cargo: "))
salarioAtual = float(input("Digite seu salário: "))
novoSalario = 0

if codigoCargo == 1:
    novoSalario = salarioAtual + (salarioAtual * .45)
    print(f"Salário atualizado: {novoSalario}")

elif codigoCargo == 2:
    novoSalario = salarioAtual + (salarioAtual * .35)
    print(f"Salário atualizado: {novoSalario}")

elif codigoCargo == 3:
    novoSalario = salarioAtual + (salarioAtual * .25)
    print(f"Salário atualizado: {novoSalario}")

elif codigoCargo == 4:
    novoSalario = salarioAtual + (salarioAtual * .15)
    print(f"Salário atualizado: {novoSalario}")

elif codigoCargo == 5:
    print("Você já recebe demais!")
else:
    print("Opção inválida!")
