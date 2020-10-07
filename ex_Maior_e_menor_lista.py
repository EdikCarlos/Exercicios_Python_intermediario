lista =[]
for c in range(0,5):
    lista.append(int(input(f'Digite o número de posição {c+1}:')))
maior = max(lista)
menor = min(lista)
print(f'O maior número da lista foi {maior} nas posições', end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f' {pos+1}...', end='')
print(f'\nO menor número da lista foi {menor} nas posições', end=' ')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'{pos+1}...', end='')

