from limpar_terminal import cls, voltar_menu

bd = {}

def linha():
    print("\n------------------------------------------\n")

def menu_alterar():
    linha()
    print("1. Nome.")
    print("2. Descrição.")
    print("3. Quantidade.")
    print("4. Preço.")
    print("5. Tudo (Cuidado, essa ação pode ser perigosa).")
    print("6. Voltar para o menu principal")
    linha()

def cadastro():
    while True:
        codigo = input("Informe o código do produto: ")
        if codigo in bd:
            linha()
            print("\nVocê está tentando cadastrar um produto já existente!\nPor gentileza selecione a opção 3 para alterar um produto.")
            linha()
            cls()
            break
        else:
            nome = input("Informe o nome do produto: ")
            descricao = input("Descrição sobre o produto: ")
            qtd = int(input("Informe a quantidade do produto:"))
            preco = float(input("Informe o preço do produto: "))
            produto = [nome,descricao,qtd,preco]
            bd[codigo] = produto
            if codigo in bd:
                print("\nProduto cadastrado com sucesso\n")
                tecla_digitada = int(input("\nDigite qualquer tecla para voltar ao menu ou 1 para cadastrar outro produto: "))
                linha()
                if tecla_digitada == 1:
                    cls()
                    continue
                else:
                    cls()
                    break
            else:
                print("Algo deu errado! Vamos tentar novamente")
                continue

def listar():
    for produto in bd:
        print(f"Produto: {produto};\nNome: {bd[produto][0]}\nDescrição: {bd[produto][1]}\nQuantidade: {bd[produto][2]}\nPreço: R${bd[produto][3]}\n")
        
    voltar_menu()

def alterar():
    codigo = input("Digite o código do produto: ")

    if codigo in bd:
        menu_alterar()
        tipo_alteracoes = int(input(f"Informe a opção que deseja alterar: "))

        if tipo_alteracoes == 1:
            nome = input(f"Digite um novo nome para o produto ({codigo}): ")
            bd[codigo][0] = nome
            voltar_menu()
        
        elif tipo_alteracoes == 2:
            descricao = input(f"Digite uma nova descrição para o produto ({codigo}): ")
            bd[codigo][1] = descricao
            voltar_menu()

        elif tipo_alteracoes == 3:
            qtd = input(f"Digite uma nova quantidade para o produto ({codigo}): ")
            bd[codigo][2] = qtd
            voltar_menu()

        elif tipo_alteracoes == 4:
            preco = input(f"Digite um novo preço para o produto ({codigo}): ")
            bd[codigo][3] = preco
            voltar_menu()
        
        elif tipo_alteracoes == 5:
            nome = input(f"Digite um novo nome para o produto ({codigo}): ")
            descricao = input(f"Digite uma nova descrição para o produto ({codigo}): ")
            qtd = input(f"Digite uma nova quantidade para o produto ({codigo}): ")
            preco = input(f"Digite um novo preço para o produto ({codigo}): ")
            bd[codigo][0] = nome
            bd[codigo][1] = descricao
            bd[codigo][2] = qtd
            bd[codigo][3] = preco
            voltar_menu()

        elif tipo_alteracoes == 6:
            voltar_menu()      
    else:
        print("Produto não cadastrado.")
        voltar_menu()
        

def buscar():
    codigo = input("Digite o código do produto: ")

    if codigo in bd:
            print(f"Produto: {codigo};\nNome: {bd[codigo][0]}\nDescrição: {bd[codigo][1]}\nQuantidade: {bd[codigo][2]}\nPreço: R${bd[codigo][3]}\n")
            voltar_menu()
    else:
        print("Produto não cadastrado!")
        voltar_menu()

def apagar():  
    codigo = input("Digite o código do produto: ")

    if codigo in bd:
        bd.pop(codigo)
        linha()
        print("Produto Apagado com sucesso!")
        linha()
        voltar_menu()
    else:
        print("Produto não cadastrado!")
        voltar_menu()


def menu ():
    print("\n---------Loja de Eletrônicos---------\n")
    print("1 . Cadastrar item")
    print("2 . Listar itens")
    print("3 . Alterar item")
    print("4 . Buscar Equipamento")
    print("5 . Apagar equipamento")
    print("6 . Sair")

def main ():
    while True:
        menu()
        opcao = int(input("\nEscolha uma opção: "))
        linha()

        if opcao == 1:
            cls()
            cadastro()
        
        if opcao == 2:
            cls()
            listar()

        if opcao == 3:
            cls()
            alterar()

        if opcao == 4:
            cls()
            buscar()
        
        if opcao == 5:
            cls()
            apagar()

        if opcao == 6:
            cls()
            break


if __name__ == '__main__':
    main()