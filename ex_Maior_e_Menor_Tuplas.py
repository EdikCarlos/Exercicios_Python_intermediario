from random import randint
sorteio = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
for n in sorteio:
    print(n, end=' ')
print(f'''\nO maior valor foi {max(sorteio)}.
O menor valor foi {min(sorteio)}.''')