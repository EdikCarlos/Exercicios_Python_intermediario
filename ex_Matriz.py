matriz = []
temp = []
for c in range(0,3):
    n = int(input(f'Digite o número de posição {[0,c]}:'))
    temp.append(n)
    matriz.append(temp[:])
    temp.clear()
for c in range(0,3):
    n = int(input(f'Digite o número de posição {[1,c]}:'))
    temp.append(n)
    matriz.append(temp[:])
    temp.clear()
for c in range(0,3):
    n = int(input(f'Digite o número de posição {[2,c]}:'))
    temp.append(n)
    matriz.append(temp[:])
    temp.clear()
print('-='*35)
print(f'''{matriz[0]} {matriz[1]} {matriz[2]}
{matriz[3]} {matriz[4]} {matriz[5]}
{matriz[6]} {matriz[7]} {matriz[8]}''')