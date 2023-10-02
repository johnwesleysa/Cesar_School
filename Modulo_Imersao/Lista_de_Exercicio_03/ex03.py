#Faça um Programa que leia um número e exiba o dia correspondente da 
#semana. (1- Domingo, 2- Segunda, etc.). Exibir mensagem “Valor 
#Inválido” caso um número inesperado for informado.

dia = int(input("Dia da semana, 1 - domingo, 2 - segunda, 3 - terça, 4 - quinta, 5 - sexta, 6 - sábado, 7 - domingo: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado.")
else: 
    print("Entrada inválida: ")