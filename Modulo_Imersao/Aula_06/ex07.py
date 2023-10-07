def conversor(horas):
    return horas*60

horas = int(input("Informe uma hora: "))
print(f"{horas} em minutos é {conversor(horas)}")