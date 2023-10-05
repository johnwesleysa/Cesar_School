"""Faça um programa que peça ao usuário para inserir:
○ uma frase
○ uma palavra que está contida na frase
○ outra palavra que ele deseja substituir no lugar da primeira palavra inserida.
Por fim, o programa exibe a frase modificada, toda em letra maiúscula."""

frase = input("Digite uma frase: ")
palavra_existente = input("Digite uma palavra existente na frase: ")
outra_palavra = input("Palavra Substituta: ")

nova_frase = frase.replace(palavra_existente, outra_palavra)
print(nova_frase.upper())