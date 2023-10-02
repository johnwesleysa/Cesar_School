codigo_alto = 0
altura_alto = 0.0
peso_alto = 0.0
codigo_baixo = 0
altura_baixo = 0.0
peso_baixo = 0.0

codigo_pesado = 0
altura_pesado = 0.0
peso_pesado = 0.0
codigo_leve = 0
altura_leve = 0.0
peso_leve = 0.0

quantidade_alunos = 0
qtd_clientes = 0
media_altura = 0.0
media_peso = 0.0
soma_altura = 0.0
soma_peso = 0.0

quantidade_alunos = int(input("Quantos clientes há na academia? "))

for i in range(quantidade_alunos):
    codigo = int(input("Digite o seu código de aluno: "))
    altura = float(input("Digite o sua altura: "))
    peso = float(input("Digite o seu peso: "))

    if i == 0:
        codigo_alto = codigo
        altura_alto = altura
        peso_alto = peso
        codigo_baixo = codigo
        altura_baixo = altura
        peso_baixo = peso
        codigo_pesado = codigo
        altura_pesado = altura
        peso_pesado = peso
        codigo_leve = codigo
        altura_leve = altura
        peso_leve = peso

    elif altura > altura_alto:
        codigo_alto = codigo
        altura_alto = altura
        peso_alto = peso

    elif altura < altura_baixo:
        codigo_baixo = codigo
        altura_baixo = altura
        peso_baixo = peso

    if peso > peso_pesado:
        codigo_pesado = codigo
        altura_pesado = altura
        peso_pesado = peso

    elif peso < peso_leve:
        codigo_leve = codigo
        altura_leve = altura
        peso_leve = peso

    qtd_clientes += 1
    soma_altura = soma_altura + altura
    soma_peso = soma_peso + peso

media_altura = soma_altura / qtd_clientes
media_peso = soma_peso / qtd_clientes

print(f"O cliente mais alto tem: código {codigo_alto}, altura {altura_alto}m e peso {peso_alto}kg.")
print(f"O cliente mais baixo tem: código {codigo_baixo}, altura {altura_baixo}m e peso {peso_baixo}kg.")
print(f"O cliente mais leve tem: código {codigo_leve}, altura {altura_leve}m e peso {peso_leve}kg.")
print(f"O cliente mais pesado tem: código {codigo_pesado}, altura {altura_pesado}m e peso {peso_pesado}kg.")
print(f"A média das alturas é: {media_altura}")
print(f"A média dos pesos é: {media_peso}")
   