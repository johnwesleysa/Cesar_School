nome = input("Nome: ")
idade= int(input("Idade:"))

if 9 <= idade <= 14:
    print(f"{nome} pode tomar vacina do HPV")
else:
    print(f"{nome} você não pode tomar a vacina")