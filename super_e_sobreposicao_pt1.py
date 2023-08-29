class MinhaString(str):
    def upper(self) -> str:
        print("chamou upper")
        retorno = super(MinhaString, self).upper()
        print("depois do upper")
        return retorno


string = MinhaString("Luiz")
print(string.upper())


class A:
    atributo_a = "Valor A"

    def metodo(self):
        print("A")


class B(A):
    atributo_B = "Valor B"

    def metodo(self):
        print("B")


class C(B):
    atributo_C = "Valor C"

    def metodo(self):
        super().metodo()
        print("C")


c = C()
print(c.atributo_C)
print(c.atributo_B)
print(c.atributo_a)
c.metodo()

