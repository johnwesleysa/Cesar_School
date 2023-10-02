#Faça um algoritmo que leia a primeira letra do estado civil de uma 
#pessoa e mostre uma mensagem com a sua descrição (Solteiro, Casado, 
#Viúvo, Divorciado). Mostre uma mensagem de erro, se necessário.

letra = input("Digite 'S' para solteiro, 'C' para casado, 'V' para viúvo, 'D' para divorciado: ")

if letra == "S":
    print("Solteiro")
elif letra == "C":
    print("Casado")
elif letra == "V":
    print("Viúvo")
elif letra == "D":
    print("Divorciado")
else:
    print("Entrada inválida!")

