def maior_idade(idade):
    if idade >= 16:
        return True
    else:
        return False
    
idade = int(input("Digite sua idade: "))

if maior_idade(idade):
    print("Pode Votar")
else:
    print("Não pode votar")