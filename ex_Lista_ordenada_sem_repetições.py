lista = []
for c in range(0,5):
    v = int(input('Digite um número: '))
    if c == 0:
        lista.append(v)
        print('Número adicionado à posição 1')
    elif v > lista[-1]:
        lista.append(v)
        print('Número adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Número adicionado à posição {pos+1}')
                break
            pos += 1
print(lista)
