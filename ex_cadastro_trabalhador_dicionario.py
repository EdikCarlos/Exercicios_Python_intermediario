from datetime import date
dados = {}
dados['Nome'] = input('Nome:')
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
dados['Idade'] = idade
ctps = int(input('Número da carteira de trabalho (Digite 0 se não tiver):'))
dados['CTPS'] = ctps
if ctps > 0:
    contr = int(input('Ano da contratação:'))
    dados['Contratação'] = contr
    sal = float(input('Salário atual:R$'))
    dados['Salário']= sal
    idade_aposentadoria = (contr - ano) + 35
    dados['Aposentadoria'] = idade_aposentadoria
print('-='*35)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')


