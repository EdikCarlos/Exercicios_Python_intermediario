print('*'*40)
print('TABELA DE PREÇOS')
print('*'*40)
lista = ('Lapis',2.50,
         'Caneta',4.00,
         'Borracha',3.30,
         'Caderno', 15.00,
         'Mochila',110.90,
         'Lancheira',35.60)
for c in range(0,len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}',end='')
    elif c % 2 == 1:
        print(f'R$ {lista[c]:>7.2f}')
print('*'*40)
