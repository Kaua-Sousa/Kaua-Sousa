# a = int(input('Entre com um Número: '))
#
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))
# a= int(input('Entre com um valor: '))
# for num in range(a+1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)
# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida. Entre com a nota Correta: '))
# a = 0
# while a <= 10:
#     print(a)
#     a += 1

a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você Digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Você Digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Você Digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto  Bimestre: '))
while d > 10:
    d = int(input('Você Digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) /4
print('media: {}'.format(media))