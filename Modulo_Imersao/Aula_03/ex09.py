for i in range(3):
    nome = input("Digite seu nome: ")
    valorTotal = float(input("Digite o valor total de compras no ano: "))
    if valorTotal < 5000:
        bonus = valorTotal * 0.1
    else:
        bonus = valorTotal * 0.15
    print(f"Olá {nome}, você possui R$ {bonus} em nossa loja")