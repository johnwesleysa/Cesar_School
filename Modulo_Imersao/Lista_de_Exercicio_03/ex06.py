#Uma rede de cinemas deseja criar um sistema para controlar a venda de 
#ingressos. Eles possuem três tipos de sessões: Matinê, Vespertina e 
#Noturna. Cada sessão tem um preço diferente. As regras são:

#1. Sessão Matinê: Custa R$ 20.
#2. Sessão Vespertina: Custa R$ 25.
#3. Sessão Noturna: Custa R$ 30.

#Crianças até 12 anos, estudantes e idosos (65+) têm direito a 50% de 
#desconto em qualquer sessão. Escreva um programa que peça ao usuário 
#para escolher o tipo de sessão e informar a idade. Caso o usuário não 
#seja idoso ou criança, ele deverá informar se é estudante. O programa 
#deve informar o valor total da compra.

sessao = int(input("Código da sessão, 1 - Matinê, 2 - Verpertina, 3 - Noturna: "))
idade = int(input("Informe sua idade: "))
desconto = .50
matine = 20
vespertina = 25
noturna = 30
valorFinal = 0


if idade >= 13 and idade <= 64:

    meia = input("Marcar S - para estudante e N - não sou estudante.")
    if sessao == 1:
        if meia == "S":
            valorFinal = matine - (matine * desconto)
            print(f"Valor do ingresso: R$ {valorFinal}")
        else:
            print(f"Valor do ingresso: R$ {matine}")
    elif sessao == 2:
        if meia == "S":
            valorFinal = vespertina - (vespertina * desconto)
            print(f"Valor do ingresso: R$ {valorFinal}")
        else:
            print(f"Valor do ingresso: R$ {vespertina}")
    elif sessao == 3:
        if meia == "S":
            valorFinal = noturna - (noturna * desconto)
            print(f"Valor do ingresso: R$ {valorFinal}")
        else:
            print(f"Valor do ingresso: R$ {noturna}")


elif idade <= 12 or idade >= 65:
    if sessao == 1:
        valorFinal = matine - (matine * desconto)
        print(f"Valor do ingresso: R$ {valorFinal}")
    elif sessao == 2:
        valorFinal = vespertina - (vespertina * desconto)
        print(f"Valor do ingresso: R$ {valorFinal}")
    elif sessao == 3:
        valorFinal = noturna - (noturna * desconto)
        print(f"Valor do ingresso: R$ {valorFinal}")

else:
    print("Entrada Inválida!")
     


