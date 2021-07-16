def numero(nota):
    while True:
        try:
            valor = float(input(nota))
        except ValueError:
            print('Isso não é um número, tente novamente!')
            continue
        else:
            return valor
            break

n1 = numero('Qual a primeira nota?: ')
while n1 > 10:
    print('O valor da primeira nota é inválida, tente novamente')
    n1 = numero('Qual a primeira nota?: ')
n2 = numero('Qual a segunda nota? ')
while n2 > 10:
    print('O valor da segunda nota é inválida, tente novamente')
    n2 = numero('Qual a segunda nota?')

media = (n1 + n2) / 2
if media == 10:
    print('Aprovado com distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
print('Sua media foi ({})'.format(media))
