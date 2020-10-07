def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


frase = input('Digite uma palavra ou frase:')
escreva(frase)
escreva(input('Digite uma palavra ou frase:'))