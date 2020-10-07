from time import sleep
lista = []
temp = []
media = []
while True:
    nome = input('Nome do aluno:')
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    lista.append(temp[:])
    temp.clear()
    med = (nota1 + nota2) / 2
    temp.append(med)
    media.append(temp[:])
    temp.clear()
    resp = input('Deseja adiconar mais alunos? [S/N]:')
    if resp in 'nN':
        break
print('-=' * 35)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for c in range(len(lista)):
    print(f'{c:<4}{lista[c][0].upper():<10}{media[c][0]:>8.2f}')
print('-' * 30)
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 para sair): '))
    if opcao == 999:
        print('FINALIZANDO...')
        sleep(2)
        break
    for n in range(len(lista)):
        if opcao == n:
            print(f'As notas de {lista[n][0].upper()} são {lista[n][1]}, {lista[n][2]}')
print('VOLTE SEMPRE!')

