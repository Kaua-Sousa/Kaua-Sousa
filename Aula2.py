a = int(input('Entre com o Primeiro Valor: '))
b = int(input('Entre com o Segundo Valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resutaldo = ('Soma: {soma}. \nSubtração: {sub}'
      '\nMultiplicação: {mult}'
      '\nDivisão: {divisao}'
      '\nresto: {resto}'.format(soma=soma, sub=subtracao, mult=multiplicacao, divisao=divisao, resto=resto))
print(resutaldo)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)