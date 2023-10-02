#Aluno: John Wesley Santos Alencar

mesMaiorVenda = ""
valorMaiorVenda = 0.0
mesMenorVenda = ""
valorMenorVenda = 0.0
somaVendasAnual = 0.0
mediaVendasAnual = 0.0

for i in range(12):
    mes = input("Digite o nome do mês: ")
    valorVendaMensal = float(input("Valor de venda mensal: "))

    if i == 0:
        mesMenorVenda = mes
        valorMenorVenda = valorVendaMensal
        mesMaiorVenda = mes
        valorMaiorVenda = valorVendaMensal
    elif valorVendaMensal < valorMenorVenda:
        mesMenorVenda = mes
        valorMenorVenda = valorVendaMensal
    elif valorVendaMensal > valorMaiorVenda:
        mesMaiorVenda = mes
        valorMaiorVenda = valorVendaMensal
    
    somaVendasAnual = somaVendasAnual + valorVendaMensal

mediaVendasAnual = somaVendasAnual / 12

print(f"Mês com a maior venda: {mesMaiorVenda} (R$ {valorMaiorVenda})")
print(f"Mês com a menor venda: {mesMenorVenda} (R$ {valorMenorVenda})")
print(f"Média de vendas ao longo do ano: R$ {mediaVendasAnual}")
print(f"Total de vendas no ano: R$ {somaVendasAnual}")

