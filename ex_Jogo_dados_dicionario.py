from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1,6),
         'Jogador 2': randint(1,6),
         'Jogador 3': randint(1,6),
         'Jogador 4': randint(1,6)}
ranking = {}
for k, v in dados.items():
    print(f'O {k} tirou o número {v} no dado.')
    sleep(1.5)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(' == RANKING ==')
for c, v in enumerate(ranking):
    print(f'{c+1}º lugar: {v[0]} com o número {v[1]}.')
    sleep(1.5)