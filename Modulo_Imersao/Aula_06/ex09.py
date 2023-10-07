def media(m):
    if m >= 7:
        print(f"Aprovado")
    else:
        print(f"Reprovado")

def media_calc(n1, n2):
    m = (n1 + n2) / 2
    return m

n1 = float(input("Digite a nota1:"))
n2 = float(input("Digite a nota2:"))

media(media_calc(n1,n2))