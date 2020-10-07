matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
soma = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor na posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print('-='*35)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*35)
print(f'A soma de todos os números pares é {par}.')
print(f'A soma dos elementos da 3ª coluna é {soma}.')
print(f'O maior número da 2ª linha é {maior}.')
