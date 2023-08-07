# Getters e Setters em Python!

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        self._cor_tampa = None

        # olha, não usem esse atributo!
        # atributos que começam em _ ou __ não devem ser usados fora da classe
        self._cor = self.cor_tinta

    # Já esse aqui seria o "getter" do python
    @property
    def cor(self):
        print("estou no getter")
        return self._cor

    # setters no python se faz assim
    @cor.setter
    def cor(self, valor):
        if valor == "Rosa":
            raise ValueError("Não aceito essa cor")
        print("Estou no setter", valor)

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


def mostrar(caneta):
    return caneta.cor


caneta = Caneta('Azul')
caneta.cor = "Pink"
print(caneta.cor_tampa)
caneta.cor_tampa = "Azul"
print(caneta.cor_tampa)
print(caneta.cor)
