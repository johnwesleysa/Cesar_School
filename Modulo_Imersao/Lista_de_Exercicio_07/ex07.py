from limpar_terminal import voltar_menu
from limpar_terminal import cls

agenda_contatos = {}

def inserir_contato(nome, numero):
    agenda_contatos[nome] = numero
    print("Contato adicionado com sucesso!")
    voltar_menu()

def excluir_contato(nome):
    agenda_contatos.pop(nome)
    print("Contato excluído com sucesso!")
    voltar_menu()

def buscar_contato(nome):
    print(f"Número de telefone de {nome}: {agenda_contatos[nome]}.")
    voltar_menu()


def menu():
    print("------Agenda de contatos------")
    print("1. Inserir contato.")
    print("2. Excluir contato.")
    print("3. Buscar contato.")
    print("4. Sair.")


def main():
    while True:
        menu()
        opcao = int(input("Digite a opção que deseja: "))
        if opcao < 1 or opcao > 4:
            print("\nInforme uma opção válida!\n")
            cls()  
            continue
        else:

            if opcao == 1:
                cls()
                nome_contato = input("Nome contato: ")
                if nome_contato in agenda_contatos:
                    print("Esse contato já está salvo!")
                    voltar_menu()
                else:
                    numero_contato = int(input("Número contato: "))
                    inserir_contato(nome_contato, numero_contato)

            elif opcao == 2:
                cls()
                nome_contato = input("Nome contato: ")
                if nome_contato in agenda_contatos:
                    excluir_contato(nome_contato)
                else:
                    print("Contato não encontrado na agenda.")
                    voltar_menu()

            elif opcao == 3:
                cls()
                nome_contato = input("Nome contato: ")
                if nome_contato in agenda_contatos:
                    buscar_contato(nome_contato)
                else:
                    print("Contato não existe!")
                    voltar_menu()

            elif opcao == 4:
                cls()
                print("Agenda: \n", agenda_contatos)
                print("Programa Finalizado.")
                break
        
if __name__ == '__main__':
    main()

