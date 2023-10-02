#Aluno: John Wesley Santos Alencar

produto = ""
qtd_produto = 0

while produto != "FIM":
    produto = input("Digite o nome do produto: ")

    #Se produto for igual a FIM, encerra o loop.
    if produto == "FIM":
        break
    
    quantidade = int(input("Digite a quantidade do produto: "))

    #Se quantidade negativa, informa um erro e retorna para qual o nome do produto.
    if quantidade < 0:
        print("Não é possível cadastro de estoque negativo.")
        continue
    
    qtd_produto += 1

print(f"Tipos de produtos cadastrados: {qtd_produto}")

