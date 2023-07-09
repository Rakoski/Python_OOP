class Pessoa:
    ano = 2023 # class attribute

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def method(cls):
        print("Aoba")

    @classmethod
    def fifty_ears(cls, nome):
        return cls(nome, 50)
    # Podemos ter acesso a própria classe sem usar o self, (sem usar a instância)

    # he @classmethod decorator specifically tells Python that the function below it is a class method, 
    # which means it belongs to the class itself, rather than to any particular object created from the class.


p1 = Pessoa("João", 35)
print(Pessoa.ano)
p2 = Pessoa.fifty_ears("Helena")
print(p2.nome, p2.idade)