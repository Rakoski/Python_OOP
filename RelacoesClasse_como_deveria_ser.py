class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


class Motor:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor10 = Motor('10')
fusca.fabricante = volkswagen
fusca.motor = motor10

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)
