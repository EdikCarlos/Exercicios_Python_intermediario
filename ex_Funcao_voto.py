from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA.')
    if 16 >= idade <18 or idade > 70:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO')

ano = int(input('Em que ano você nasceu?:'))
voto(ano)