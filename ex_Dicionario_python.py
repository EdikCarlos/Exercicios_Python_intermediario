dados = {}
dados['Nome'] = str(input('Nome:'))
dados['Media']= float(input((f'Média de {dados["Nome"]}:')))
if dados['Media'] < 7:
    dados['Situação'] = '\033[31mREPROVADO\033[m'
else:
    dados['Situação'] = '\033[32mAPROVADO\033[m'
print('-='*30)
print(f'- O nome do aluno é {dados["Nome"]}.')
print(f'- Sua média foi {dados["Media"]}.')
print(f'- Sua situação é {dados["Situação"]}.')