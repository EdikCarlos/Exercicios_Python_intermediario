lista = []
pessoas = []
cont = 0
gordo = 0
magro = 1000
while True:
    pessoas.append(input('Nome:'))
    pessoas.append(float(input('Peso:')))
    lista.append(pessoas[:])
    pessoas.clear()
    cont += 1
    resp = input('Deseja continuar?[S/N]').upper().strip()
    for c in lista:
        if c[1] > gordo:
            gordo = c[1]
        elif c[1] < magro:
            magro = c[1]
    if resp == 'N':
        break
print('-='*40)
print(f'Ao todo foram cadastradas {cont} pessoas.')
print(f'O maior peso foi de {gordo}Kg do(s) individuo(s): ',end='')
for p in lista:
    if p[1] == gordo:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {magro}Kg do(s) individuo(s): ',end='')
for p in lista:
    if p[1] == magro:
        print(f'[{p[0]}]', end=' ')