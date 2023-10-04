#Alunos: Rogerio Fernandes, John Wesley, Matheus Antônio

nota1 = 0.0
nota2 = 0.0
vetorMedia = []
qtdMaiorMedia = 0

for i in range(5):
    nota1 = float(input("Digite a nota1: "))
    nota2 = float(input("Digite a nota2: "))
    media = (nota1 + nota2) / 2
    vetorMedia.append(media)

print(f"Médias: {vetorMedia}")

for i in vetorMedia:
    if i >= 7:
        qtdMaiorMedia +=1 

print(f"Número de estudantes com média >= 7: {qtdMaiorMedia}")