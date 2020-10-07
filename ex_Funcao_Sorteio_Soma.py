from random import randint
números = []


def sorteia():
    cont = 0
    print(f'Sorteando 5 valores da lista: ', end='')
    for v in range(0, 5):
        números.append(randint(1, 10))
        print(números[cont], end=' ')
        cont += 1
    print('PRONTO!')


def somapar():
    print(f'Somando os valores pares de {números}, temos ',end='')
    totpar = 0
    cont = 0
    for n in números:
        if números[cont] % 2 == 0:
            totpar += números[cont]
        cont += 1
    print(totpar)





sorteia()
somapar()