# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
#
# if a > b:
#     print('O Maior Numero é {}'.format(a))
# else:
#     ('O Maior Numero é {}'.format(b))
#
# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro Valor: '))
#
# if a > b and a > c:
#     print('O Maior Numero é {}'.format(a))
# elif b > a and b > c:
#   print('O Maior Numero é {}'.format(b))
# else:
#     print('O Maior Numero é {}'.format(c))
# print('Final Do Programa')

# a = int(input('Entre com o Primeiro Numero: '))
# b = int(input('Entre com o Segundo Numero: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi Digitado um Numero Par')
# else:
#     print('Não foi Digitado nenhum Numero par')
a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você Digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b> 10:
    b = int(input('Você Digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Você Digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto  Bimestre: '))
if d > 10:
    d = int(input('Você Digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) /4
print('media: {}'.format(media))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada')
