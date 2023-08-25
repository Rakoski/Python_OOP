class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])  # retorna a soma de algum array com números

    def inserir_produtos(self, *produtos):  # insere algum produto no carrinho

        # todas essas resultam na mesma coisa
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):  # http GET
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    # propriedades dos produtos
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())