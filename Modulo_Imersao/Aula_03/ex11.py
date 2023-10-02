nomeMelhorDesempenho = ""
notaMelhorDesempenho = 0.0
nomePiorDesempenho = ""
notaPiorDesempenho = 0.0
somaNota = 0.0
qtdAlunos = 0

for i in range(5):

    nome = input(f"Digite o nome do estudade {i + 1}: ")
    nota = int(input(f"Digite a nota do estudante {i + 1}: "))

    if i == 0:
        nomeMelhorDesempenho = nome
        notaMelhorDesempenho = nota
        nomePiorDesempenho = nome
        notaPiorDesempenho = nota
    elif nota < notaPiorDesempenho:
        notaPiorDesempenho = nota
        nomePiorDesempenho = nome
    elif nota > notaMelhorDesempenho:
        notaMelhorDesempenho = nota
        nomeMelhorDesempenho = nome
    
    qtdAlunos += 1
    somaNota = somaNota + nota

media = somaNota / qtdAlunos 
print(f"{nomeMelhorDesempenho} com melhor desempenho, com nota de {notaMelhorDesempenho}")
print(f"{nomePiorDesempenho} com pior desempenho, com nota de {notaPiorDesempenho}")
print(f"A média da turma foi {media}")

    
