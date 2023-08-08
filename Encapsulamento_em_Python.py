# Em python, não existe essa coisa de public, private e protected, como há em java.
# Para podermos então fazer tal distinção, usamos as underlines.
# Public - public (sem underline)
# Protected - _protected (1 underline)
# Private - __private (2 underlines)

class Foodeu:
    def __init__(self):
        self.publico = "Isso é público"
        self._protected = "Isso é protegido"
        self.__private = "Isso é privado"

    def metodo_publico(self):
        self.__metodo_private()
        print(self._protected)  # agora ta certo!
        return "Isso é um método público"

    def __metodo_private(self):
        print("isso é privado")
        return "Isso é privado"


foo = Foodeu()  # Instânciando a classe
print(foo.publico)
print(foo.metodo_publico())
# print(foo._protected)  # Não era pra isso aqui acontecer, e nem pode em outras linguagens, como java e C#
# Se eu realmente quiser acessar algo privado, de fora da classe, tem o "name mangling" que te ferra, olha como fica
# print(foo._Foodeu__metodo_private())
