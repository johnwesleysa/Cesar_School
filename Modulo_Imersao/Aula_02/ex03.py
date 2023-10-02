nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (f - feminino, m - masculino): ")
idade = int(input("idade: "))
if (sexo == 'm' and idade >= 18):
    print(f"Olá, {nome}, você está apto")