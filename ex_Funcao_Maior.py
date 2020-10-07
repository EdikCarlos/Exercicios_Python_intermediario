def linha():
    print('-='*30)


def maior(*n):
    linha()
    print('Analisando os valores passados...')

    for v in n:
        print(f'{v}', end=' ')
    print(f'Foram informados {len(n)} valores ao todo.')
    m = -99999
    for v in n:
        if v > m:
            m = v
    if len(n) == 0:
        print('Não tiveram valores informados.')
    else:
        print(f'O maior valor informado foi {m}.')



r1 = maior(2, 17, 4, 9, 11)
r2 = maior(13, 16, 29, 33)
maior(0, 5, 3)
maior(-32, -87, -3, -1)
maior()
print(f'Os maiores são {r1} e {r2}')


