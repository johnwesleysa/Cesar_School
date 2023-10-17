
media_tempo_pilotos = {}
melhor_media = [[],[]]
campeao = {}

for i in range(4):
    nome_piloto = input("Nome piloto: ")
    lista_tempo = []
    for j in range(3):
        tempo_segundos_corrida = float(input("Digite o tempo em segundos da corrida: "))
        lista_tempo.append(tempo_segundos_corrida)
    
    media_tempo_pilotos[nome_piloto] = lista_tempo
    
    media = sum(media_tempo_pilotos[nome_piloto]) / 3
    if i == 0:
        melhor_media[0] = nome_piloto
        melhor_media[1] = media
    elif media < melhor_media[1]:
        melhor_media[0] = nome_piloto
        melhor_media[1] = media

print(f"O campeão é {melhor_media[0].upper()} com média de tempo de {melhor_media[1]:.2f} segundos.")