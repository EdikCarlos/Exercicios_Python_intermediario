lista = [[],[]]
for c in range(0,7):
    v = int(input(f'Digite o {c+1}º valor:'))
    if v % 2 == 0:
        lista[0].append(v)
    if v % 2 == 1:
        lista[1].append(v)
print(f'Os números pares digitados foram {sorted(lista[0])}')
print(f'Os números ímpares digitados foram {sorted(lista[1])}')





