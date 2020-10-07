def area(l, c):
    area = l * c
    print(f'A área do terreno com as medidas {l}m e {c}m é de {area}m²')


print(f'{"Controle de Terrenos"}')
print(f'-'*35)
l = float(input('Digite a largura do terreno:'))
c = float(input('Digite o comprimento do terreno:'))
area(l, c)