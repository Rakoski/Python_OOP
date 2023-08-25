# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# um motor pode ser de vários carros e um fabricante pode fabricar vários carros

class Carro:
    def __init__(self, nome):
        self.nome = nome


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def inserir_carro(self, nome_carro):
        self.carros.append(Carro(nome_carro))

    def listar_carros(self):
        for carro in self.carros:
            print(carro.nome)


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def inserir_carro(self, nome_carro):
        self.carros.append(Carro(nome_carro))

    def listar_carros(self):
        for carro in self.carros:
            print(carro.nome)


corsa = Carro('Corsa')
fabricante = Fabricante('GM')
fabricante.inserir_carro(corsa.nome)

motor = Motor('V8')
v8 = Carro('F. Enzo')
motor.inserir_carro(v8.nome)

fabricante.listar_carros()
motor.listar_carros()



