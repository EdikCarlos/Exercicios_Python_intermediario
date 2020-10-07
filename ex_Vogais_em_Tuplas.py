palavras = ('Helena', 'Edik','Jacqueline','Caroline','Simone','Terezinha')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos: ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')