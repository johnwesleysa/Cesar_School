lista_alunos = []


for i in range(4):
    nomes = input("Nome Aluno: ")
    notas = []
    for j in range(3):
        notas.append(float(input(f"Digite a nota {j + 1} do estudante {nomes}: ")))
    
    media = sum(notas) / len(notas)

    lista_alunos.append((nomes, media))

print(lista_alunos)