lista = []
pares = []
impar = []
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impar.append(n)
    resp = input('Quer continuar?[S/N]').upper().strip()
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impar}')