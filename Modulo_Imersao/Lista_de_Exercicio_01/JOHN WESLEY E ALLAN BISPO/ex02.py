produto = float(input("Insira o valor do produto: "))
desconto = float(input("Insira o valor do desconto: "))
calc = produto - (produto * (desconto/100))

print(f"Valor com desconto: R$ {calc}")

