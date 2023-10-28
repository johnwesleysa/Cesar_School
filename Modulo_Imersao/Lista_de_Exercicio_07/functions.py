#pega numero inteiro

def get_int():
    while True:
        try:
            num_int = int(input("Digite um número inteiro: "))
            break
        except:
            print("Isso não é um número inteiro!")
            continue
    return num_int
        
def get_float():
    while True:
        try:
            num_float = float(input("Digite um número: "))
            break
        except:
            print("Isso não é um número")
            continue
    return num_float
        
