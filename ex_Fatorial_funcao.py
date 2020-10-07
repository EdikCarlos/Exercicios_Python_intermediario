def funcao(n=1, show=False):
    """
    -> Calcula o fatorial de um número(n).
    :param n: Número positivo e maior que zero.
    :param show: (opcional) True = Mostra toda a conta realizada.
    :return: Retorna o valor do fatorial do número n.
    """
    f = 1
    tot = 1
    if n == 0:
        print('Digite um valor acima de zero.')
    if n < 0:
        print('Digite um número positivo')
    else:
        if show == True:
            while n > 0:
                print(f'{n}', end='')
                print(f' x ' if n > 1 else ' = ', end='')
                f *= n
                n -= 1
            return print(f'{f}')
        if show ==  False:
            while n > 0:
                f *= n
                n -= 1
            return print(f'{f}')


n = int(input('Digite um número acima de 0 para ver seu fatorial:'))
funcao(n, True)