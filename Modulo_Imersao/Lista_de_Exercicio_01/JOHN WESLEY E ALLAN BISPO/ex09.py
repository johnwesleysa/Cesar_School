valorProduto = float(input("Valor produto: "))
taxa = float(input("Taxa de imposto: "))

calc = valorProduto + (valorProduto * (taxa/100))

print(f"Valor Final com Imposto: {calc}")