def calcular_media_tempos(tempos):
    return sum(tempos) / len(tempos)

def encontrar_melhor_volta(corredores):
    menor_tempo = float('inf')
    melhor_volta = 0
    melhor_corredor = None
    
    for corredor, tempos in corredores.items():
        min_tempo = min(tempos)
        if min_tempo < menor_tempo:
            menor_tempo = min_tempo
            melhor_volta = tempos.index(min_tempo) + 1
            melhor_corredor = corredor
    
    return melhor_corredor, melhor_volta

def classificacao_final(corredores):
    return sorted(corredores, key=lambda corredor: calcular_media_tempos(corredores[corredor]))

corredores = {}

for i in range(6):
    nome = input(f"Digite o nome do corredor {i + 1}: ")
    tempos = []
    for volta in range(1, 11):
        tempo = float(input(f"Digite o tempo da volta {volta} em segundos: "))
        tempos.append(tempo)
    corredores[nome] = tempos

melhor_corredor, volta_melhor = encontrar_melhor_volta(corredores)
classificados = classificacao_final(corredores)

print(f"\nMelhor volta da prova: {melhor_corredor}, na volta {volta_melhor}")
print("\nClassificação final:")
for posicao, corredor in enumerate(classificados, start=1):
    media = calcular_media_tempos(corredores[corredor])
    print(f"{posicao}º - {corredor}: Média de tempos = {media:.2f} segundos")
