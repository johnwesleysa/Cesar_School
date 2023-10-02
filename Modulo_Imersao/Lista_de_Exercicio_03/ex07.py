#● Plano Básico: 100 minutos e 5GB de internet por R$ 50.
#● Plano Intermediário: 300 minutos e 10GB de internet por R$ 80.
#● Plano Avançado: 500 minutos e 20GB de internet por R$ 120.

#Caso o cliente ultrapasse a franquia de minutos, será cobrado R$ 1 por 
#minuto adicional. Se ultrapassar a franquia de internet, será cobrado 
#R$ 10 por GB adicional. Escreva um programa que peça ao usuário para 
#escolher um plano, informar quantos minutos e quantos GB ele utilizou 
#no mês. O programa deve calcular e mostrar o valor total da fatura.


#inputs, pedindo plano de tv, tempo em minutos e gb por mês
plano = input("Qual plano: ")
minutos = int(input("Quantos minutos: "))
gb = float(input("Quantos GB:"))
gbAdd = 0
minutosAdd = 0
fatura = 0

#condicionais
if plano == 'Básico':
    if minutos <= 100 and gb <= 5:
        print(f"Valor da fatura: R${50}")

    else: 
        if gb > 5:
            gbAdd = (gb - 5) * 10
        if minutos > 100:
            minutosAdd = (minutos - 100) * 1
        fatura = 50 + gbAdd + minutosAdd
        print(f"Valor da fatura: R${fatura}")

elif plano == 'Intermediário':
    if minutos <= 300 and gb <= 10:
        print(f"Valor da fatura: R${80}")
    else: 
        if gb > 10:
            gbAdd = (gb - 10) * 10
        if minutos > 300:
            minutosAdd = (minutos - 300) * 1
        fatura = 80 + gbAdd + minutosAdd
        print(f"Valor da fatura: R${fatura}")

elif plano == 'Avançado':
    if minutos <= 500 and gb <= 20:
        print(f"Valor da fatura: R${120}")
    else: 
        if gb > 20:
            gbAdd = (gb - 20) * 10
        if minutos > 500:
            minutosAdd = (minutos - 500) * 1
        fatura = 120 + gbAdd + minutosAdd
        print(f"Valor da fatura: R${fatura}")

else: 
    print("Entrada inválida!")



        


    


