from Aula7_Televisao import Televisao
from Aula7_Calculadora1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora (10,7)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra da lista: {}'.format(total_letras))