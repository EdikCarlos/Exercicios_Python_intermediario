from time import sleep
def contador(inicio, fim, passo):
    linha()
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if fim < inicio and passo > 0:
       fim -= 1
       passo *= -1
    elif passo < 0:
        fim -= 1
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='')
        sleep(0.5)
    print('FIM')
    linha()


def linha():
    print('-='*30)



linha()
print('Contagem de 1 a 10 de 1 em 1.')
for c in range(1, 11):
    print(f'{c} ',end='')
    sleep(0.5)
print('FIM')
linha()
print('Contagem de 10 até 0 de 2 em 2.')
linha()
for c in range(10, -1, -2):
    print(f'{c} ', end='')
    sleep(0.5)
print('FIM')
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('INICIO:'))
f = int(input('FIM:'))
p = int(input('PASSO:'))
contador(i,f,p)