from limpar_terminal import voltar_menu
from limpar_terminal import cls

produtos_em_estoque = {}
#retorna 0 caso o produto exista no estoque
def verifica_produto_em_estoque(produto):
    if produto in produtos_em_estoque:
        return 0
    else: 
        return 1   

def incluir_produto(nome, quantidade, valor):
    produtos_em_estoque[nome] = [quantidade, valor]
    print(f'Produto "{nome.capitalize()}" adicionado ao estoque.')
    voltar_menu()

def excluir_produto(nome):
    produtos_em_estoque.pop(nome)
    print(f"{nome.capitalize()} exluído com sucesso do estoque.")
    voltar_menu()

def atualizar_estoque(nome, qtd):
    produtos_em_estoque[nome][1] = qtd
    print(f'Estoque de "{nome}" atualizado para {qtd} unidades.')
    voltar_menu()

def exibir_estoque():
    print("Lista de Produtos em Estoque: ")
    for produto in produtos_em_estoque:
        print(f"Nome: {produto.capitalize()}")
        print(f"Quantidade em estoque: {produtos_em_estoque[produto][0]} unidades")
        print(f"Preço Unitário: R$ {produtos_em_estoque[produto][1]:.2f}")
    voltar_menu()
     
def calcular_valor_total():
    soma = 0.0
    valor_total_produtos = 0.0
    for produto in produtos_em_estoque:
        valor_total_produtos = (produtos_em_estoque[produto][0] * produtos_em_estoque[produto][1])
        soma = soma + valor_total_produtos
    print(f"Valor total do estoque: R$ {soma:.2f}")
    voltar_menu()



def menu():
    print("Estoque")
    print("1. Incluir produto.")
    print("2. Excluir produto.")
    print("3. Atualizar estoque.")
    print("4. Exibir todo o estoque.")
    print("5. Calcular Valor total do estoque.")
    print("6. Sair: Encerra o programa.")

def main():
    while True:
        menu()
        opcao = int(input("Informe a opção desejada: "))
        if opcao < 1 or opcao > 7:
            print("Opção inválida!")
            cls()
            continue
        else:

            #incluir
            if opcao == 1:
                cls()
                nome = input("Nome produto: ")

                if verifica_produto_em_estoque(nome) == 0:
                    print(f"Produto {nome:.capitalize()} já existe em estoque")
                else:
                    qtd = int(input("Quantidade produto: "))
                    valor = float(input("Valor produto: "))
                    incluir_produto(nome, qtd, valor)
            
            #exluir
            elif opcao == 2:
                cls()
                nome = input("Nome produto: ")
                if verifica_produto_em_estoque(nome) == 1:
                    print(f"Produto {nome:.capitalize()} não existe no estoque.")
                else:
                    excluir_produto(nome)

            elif opcao == 3:
                cls()
                nome = input("Nome produto: ")
                if verifica_produto_em_estoque(nome) == 1:
                    print(f"Produto {nome:.capitalize()} não existe no estoque.")
                else:
                    qtd = int(input("Nova quantidade: "))
                    atualizar_estoque(nome, qtd)

            elif opcao == 4:
                cls()     
                exibir_estoque()

            elif opcao == 5:
                cls()
                calcular_valor_total()
            elif opcao == 6:
                cls()
                print("Programa Finalizado!")
                break

if __name__ == '__main__':
    main()