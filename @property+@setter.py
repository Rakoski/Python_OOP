class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

        # olha, não usem esse atributo!
        # atributos que começam em _ ou __ não devem ser usados fora da classe
        self._cor = self.cor_tinta


    @property
    def cor(self):
        print('property')
        return 'Qualquer'

    @cor.setter
    def cor(self, valor):
        print("Estou no setter", valor)


def mostrar(caneta):
    return caneta.cor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
print(caneta.cor)
