dados = {}
gols = []
totgol = 0
cont = 0
dados['Nome'] = input('Nome do jogador:')
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou?: '))
print('-='*30)
for g in range(partidas):
    gol = int(input(f'Quantos gols na partida {g+1}?'))
    gols.append(gol)
    totgol += gol
    dados['Gols'] = gols
    dados['Total'] = totgol
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for p in range(partidas):
    print(f'=> Na partida {p+1}, fez {gols[cont]} gols. ')
    cont += 1
print(f'Foi um total de {totgol} gols.')