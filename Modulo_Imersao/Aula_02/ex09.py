idade = int(input("Idade: "))

if 0 <= idade <= 12:
    print(f"Criança")
elif 12 < idade <= 20:
    print("Adolescente")
elif 20 < idade <= 64:
    print("Adulto")
elif idade > 64:
    print("Idoso")
else:
    print("Idade Inválida")