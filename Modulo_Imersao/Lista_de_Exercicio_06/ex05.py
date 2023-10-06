"""
Faça um programa que leia um número de celular, e corrija o número no caso deste conter somente 8 dígitos, adicionando o '9' na frente. O usuário pode informar o número com ou sem o traço separador.
"""

while True:
    numero = input("Número celular: ")
    if len(numero)< 8:
        print("Insira um número válido!")
        continue

    if len(numero) == 8 or (len(numero) == 9 and '-' in numero):
        novo_numero = '9'+numero
        print(novo_numero)
    else: 
        print(numero)
    
    break