extenso = ('zero', 'hum', 'dois', 'três','quatro', 'cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('Digite um número entre 0 e 20:'))
#while True:
if n > 20:
    n = int(input('ERRO:Tente novamente. Digite um número entre 0 e 20:'))
print(f'Você digitou o número {extenso[n]}.')
while True:
    resp = str(input('Deseja escolher um novo número? [S/N]')).upper().strip()
    if resp == 'S':
        n = int(input('Digite um número entre 0 e 20:'))
        while n > 20:
            n = int(input('ERRO:Tente novamente. Digite um número entre 0 e 20:'))
        print(f'Você digitou o número {extenso[n]}.')
    else:
        break
print('Obrigado por utilizar o programa, volte sempre!')