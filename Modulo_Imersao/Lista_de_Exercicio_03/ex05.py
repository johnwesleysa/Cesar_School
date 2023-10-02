#Um hotel de luxo deseja automatizar seu sistema de reservas. Eles 
#possuem três tipos de suítes: Standard, Luxo e Presidencial. Cada tipo 
#de suíte tem uma quantidade limitada de noites que pode ser reservada a 
#um preço diferente. O hotel definiu as seguintes regras:

#1. Suíte Standard: Custa R$ 250 por noite, limite de 15 noites.
#2. Suíte Luxo: Custa R$ 500 por noite, limite de 10 noites.
#3. Suíte Presidencial: Custa R$ 1200 por noite, limite de 7 noites.

#Além disso, se o cliente desejar ficar 5 noites ou mais, ele recebe um 
#desconto de 10% no valor total, independentemente do tipo de suíte 
#escolhida. Escreva um programa que peça ao usuário para escolher o tipo 
#de suíte, a quantidade de noites e informe o valor total da estadia. Se 
#a quantidade de noites informada for maior que o limite disponível, ]
#informe ao usuário e finalize o sistema.

suite = int(input("Qual suíte, digite '1' para Standard, '2' para Luxo, '3' para presidencial: "))
if suite <= 0 or suite >= 4:
    print("Opção inválida!")
else:
    qtdNoites = int(input("Quantidade de noites: "))
    standard = 250
    luxo = 500
    presidencial = 1200
    desconto = .10
    valor = 0



    if suite == 1 and qtdNoites <= 15:
        if qtdNoites > 15:
            print("Limite de noites atingido")
        valor = standard * qtdNoites    
        if qtdNoites >= 5:
            desconto = valor - ( valor * desconto)
            print(f"Valor total da estadia: R$ {desconto}")
        else:
            print(f"Valor total da estadia: R$ {valor}")

    elif suite == 2 and qtdNoites <= 10:
        if qtdNoites > 10:
            print("Limite de noites atingido")
        valor = luxo * qtdNoites
        if qtdNoites >= 5 :
            desconto = valor - (valor * desconto)
            print(f"Valor total da estadia: R$ {desconto}")
        else:
            print(f"Valor total da estadia: R$ {valor}")

    elif suite == 3 and qtdNoites <= 7:
        if qtdNoites > 7:
            print("Limite de noites atingido")
        valor = presidencial * qtdNoites
        if qtdNoites >= 5:
            desconto = valor - (valor * desconto)
            print(f"Valor total da estadia: R$ {desconto}")
        else: 
            print(f"Valor total da estadia: R$ {valor}")
        


