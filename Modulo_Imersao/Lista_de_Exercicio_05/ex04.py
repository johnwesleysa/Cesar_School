#Faça um programa que:
# ○ Receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# ○ Calcule a média anual de temperaturas
# ○ Exiba todos os meses que têm as temperaturas acima da média anual (mostrar o mês por extenso: Janeiro, Fevereiro, . . . ). Dica: Crie uma lista de strings com todos os nomes dos meses.

meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media_temperatura_mensal = []
media_temperatura_anual = 0.0

for i in range(12):
    media_temperatura_mensal.append(float(input(f"Média temperatura {meses_ano[i]}: ")))

#media anual de temp
media_temperatura_anual = sum(media_temperatura_mensal) / 12
print(f"\nMédia Anual de Temperaturas: {media_temperatura_anual}")

print("Meses com temperaturas acima da média:")
for i in range(len(media_temperatura_mensal)):
    if media_temperatura_mensal[i] > media_temperatura_anual:
        print(meses_ano[i])
        


