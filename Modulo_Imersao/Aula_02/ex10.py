num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))
num4 = int(input("Num4: "))
contPar = 0
contImpar = 0

if num1 % 2 == 0:
    contPar += 1
else:
    contImpar += 1


if num2 % 2 == 0:
    contPar += 1
else:
    contImpar += 1


if num3 % 2 == 0:
    contPar += 1
else:
    contImpar += 1

    
if num4 % 2 == 0:
    contPar += 1
else:
    contImpar += 1

print(f"Number pares: {contPar}")
print(f"Numbers Impares: {contImpar}")