#Faça um programa que receba um e-mail e verifique se ele é válido. Obs: Para um
#e-mail ser válido considerar se possui “@”.

email = input("Digite seu e-mail: ")

if '@' in email:
    print("E-mail válido.")
else:
    print("E-mail inválido.")