frase = input("Frase: ")
palavra = input("palavra: ")

if palavra in frase:
    frase2 = frase.replace(palavra, "domingo")
    print(f"Houve modificação: {frase2}")
else:
    print(f"Não houve alteração: {frase}")

