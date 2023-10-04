#Alunos: Rogerio Fernandes, John Wesley, Matheus Antônio
#Faça um programa que:
#○ Peça duas notas de 5 estudantes.
#○ Calcule e armazene numa lista a média de cada estudante.
#○ Imprima a lista de médias;
#○ Imprima o número de estudantes com média >= 7.0.

nota1 = 0.0
nota2 = 0.0
medias = []
qtd_acima_media = []

for i in range(5):
    nota1 = float(input(f"1° Nota: "))
    nota2 = float(input(f"2° Nota: "))

    medias.append((nota1 + nota2) / 2)

for i in medias:
    if i >= 7:
        qtd_acima_media.append(i)

print(f"Médias: {medias}")
print(f"Número de estudantes com média >= 7: {len(qtd_acima_media)}")


  