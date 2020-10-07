from time import sleep
dados = {}
lista = []
soma_idade = 0
while True:
    dados['Nome'] = input('Nome:').strip()
    dados['Idade'] = int(input('Idade:').strip())
    soma_idade += dados['Idade']
    dados['Sexo'] = input('Sexo [M/F]:').upper().strip()
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = input('Por favor, digite apenas [M/F]:').upper().strip()
    lista.append(dados.copy())
    resp = input('Deseja continuar? [S/N]:').upper().strip()
    while resp not in 'SN':
        resp = input('ERRO: Deseja continuar? [S/N]:').upper().strip()
    if resp == 'N':
        break
print('-='*35)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é {soma_idade / len(lista):.2f} anos.')
print(f'C) As mulheres Cadastradas foram: ',end='')
for c in lista:
    if c['Sexo'] == 'F':
        print(f'[{c["Nome"].title()}]',end=' ')
print(f'\nD) Lista das pessoas que tem idade acima da média: ',end='')
for k, v in enumerate(lista):
    if v['Idade'] > soma_idade / len(lista):
        print(f'    \nNome = {v["Nome"].title()}; Sexo = {v["Sexo"]}; Idade = {v["Idade"]}',end='')
print('\nENCERRANDO...')
sleep(2)
