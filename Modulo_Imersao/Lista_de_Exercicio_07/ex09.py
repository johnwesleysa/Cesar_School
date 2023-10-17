from limpar_terminal import voltar_menu
from limpar_terminal import cls

contas = {}

#retorna 0 caso a conta exista
def verifica_conta(conta):
    if conta in contas:
        return 0
    else: 
        return 1   
    
def criar_conta(conta, nome, saldo_inicial):
    contas[conta] = [nome, saldo_inicial]
    print("Conta criada com sucesso.")
    voltar_menu()

def consultar_saldo(conta):
    print(f"Saldo em conta: {contas[conta][1]}")
    voltar_menu()

def saque(conta, valor_saque):
    if contas[conta][1] >= valor_saque:
        contas[conta][1] = contas[conta][1] - valor_saque
        print("Saque realizado com sucesso.")
        voltar_menu()
    else:
        print("Saldo insuficiente.")
        voltar_menu()

def deposito(conta, valor_deposito):
    contas[conta][1] = contas[conta][1] + valor_deposito
    print("Depósito realizado com sucesso.")
    voltar_menu()

def menu():
    print("Banco")
    print("Digite 1 para criar uma nova conta. ")
    print("Digite 2 para consultar o saldo de uma conta específica. ")
    print("Digite 3 para realizar um saque em uma conta.")
    print("Digite 4 para realizar um depósito em uma conta. ")
    print("Digite 5 para sair do programa")

def main():
    while True:
        menu()
        opcao = int(input("Informe a opção desejada: "))
        if opcao < 1 or opcao > 5:
            print("Opção inválida!")
            cls()
            continue
        else:

            #criar conta
            if opcao == 1:
                cls()
                conta = input("Código da conta: ")

                if verifica_conta(conta) == 0:
                    print(f"Conta {nome:.capitalize()} já existe!")
                else:
                    nome = input("Nome titular: ")
                    saldo_inicial = float(input("Saldo inicial: "))
                    criar_conta(conta, nome, saldo_inicial)
            
            #consulta saldo de uma conta
            elif opcao == 2:
                cls()
                conta = input("Código da conta: ")
                if verifica_conta(conta) == 1:
                    print(f"Conta não encontrada.")
                    cls()
                else:
                    consultar_saldo(conta)

            elif opcao == 3:
                cls()
                conta = input("Código da conta: ")
                if verifica_conta(conta) == 1:
                    print(f"Conta não encontrada.")
                    cls()
                else:
                    valor_saque = float(input("Digite o valor do saque: "))
                    saque(conta, valor_saque)

            elif opcao == 4:
                cls()     
                conta = input("Código da conta: ")
                if verifica_conta(conta) == 1:
                    print(f"Conta não encontrada.")
                    cls()
                else:
                    valor_deposito = float(input("Valor deposito: "))
                    deposito(conta, valor_deposito)

            
            elif opcao == 5:
                cls()
                print("Programa Finalizado!")
                break

if __name__ == '__main__':
    main()



