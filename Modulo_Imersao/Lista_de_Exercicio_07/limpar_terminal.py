import os

def cls():
    os.system("cls")

def voltar_menu():
    tecla = (input("Digite qualquer tecla para voltar ao menu: "))
    if tecla != 0:
        cls()

        