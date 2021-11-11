lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10/0
    numero = lista[1]
   except ZeroDivisionError:
    print('Não é possivel realiar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não a nenhum erro no bloco')
finally:
    print('semrpe executa')
    print('fechando arquivo')
    arquivo.close()
