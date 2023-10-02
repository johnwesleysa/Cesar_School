salario = float(input("Digite seu salário: "))
admissao = int(input("Digite o seu ano de admissão: "))
ultimoReajuste = int(input("Digite o último ano de reajuste: "))

ANO_ATUAL = 2023

tempoReajuste = ANO_ATUAL - ultimoReajuste

if tempoReajuste >= 2:
    ano_casa = ANO_ATUAL - admissao
    if ano_casa >= 10:
        reajuste = salario * (salario * 0.3)
    elif 10 >= ano_casa >= 5:
        reajuste = salario + (salario * 0.2)
    else:
        reajuste = salario + (salario * 0.1)
    print(f"Novo Salário: {reajuste}")
else:
    print("Não está apto ao reajuste salárial coletivo")