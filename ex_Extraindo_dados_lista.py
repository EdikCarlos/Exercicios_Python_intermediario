lista = []
cont = 0
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    cont += 1
    resp = str(input('Deseja digitar outro número?[S/N]:')).upper().strip()
    if resp == 'N':
        break
print('*'*50)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não está na lista.')


