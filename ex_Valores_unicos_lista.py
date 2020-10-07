lista = []
while True:
    v = int(input('Digite um valor: '))
    if v not in lista:
        lista.append(v)
    else:
        print('\033[31mValor duplicado, não irei adicionar.\033[m')
    r = str(input('Deseja continuar? [S/N]:')).upper().strip()
    if r == 'N':
        break
    while r != 'S':
        r = str(input('Erro. Deseja continuar? [S/N]:')).upper().strip()
    if r == 'N':
        break
print(sorted(lista))