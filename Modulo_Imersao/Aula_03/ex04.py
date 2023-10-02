idade = 0
contIdade = 0

while idade != -1 :
    idade = int(input("Digite sua idade: "))
    if idade == -1:
        break
    else:
        contIdade += 1
    
print(f"idades validas: {contIdade}")


    