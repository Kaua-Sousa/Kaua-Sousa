class Calculadora:
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(10, 2))
    print(calculadora.subtracao(50, 20))
    print(calculadora.multiplicacao(100, 2))
    print(calculadora.divisao(1000, 500))
