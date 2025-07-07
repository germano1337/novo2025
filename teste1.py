'''calculadora de média'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média é: {media:.1f}')

'''verifica se a média é maior ou igual a 7.0'''
if media >= 7.0:
    print('Aprovado')
else:
    print('Reprovado')