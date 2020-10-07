n = (int(input('Digite um número de 0 a 9:')),int(input('Digite um número de 0 a 9:')),int(input('Digite um número de 0 a 9:')),int(input('Digite um número de 0 a 9:')))
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu pela primeira vez na {n.index(3)+1}ª posição.')
else:
    print('Não foi digitado o número 3.')
print('Os valores pares digitados foram: ',end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')