class Erro(Exception):
    pass
class InputErro(Erro):
    def __init__(self, menssage):
        self.menssage = menssage

while True:
    try:
        x = int(input('Entre com um numero de 0 á 10: '))
        print(x)
        if x > 10:
            raise InputErro('A nota não pode ser maior que 10')
        elif x < 0:
            raise InputErro('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor invalido . deve-se digitar apenas números.')
    except InputErro as ex:
        print(ex)