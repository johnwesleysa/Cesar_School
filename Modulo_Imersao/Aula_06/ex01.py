#Function em python é sempre antes do programa principal
def bom_dia_user(nome):
    print("Olá, Bom dia!")
    return f"Bem-vindo(a), {nome}"

nome = input("Digite seu nome: ")
print(bom_dia_user(nome))




