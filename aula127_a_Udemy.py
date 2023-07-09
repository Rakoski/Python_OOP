import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('José', 12)
p3 = Pessoa('Maria', 27)
bd = [vars(p1), vars(p2), vars(p3)]

# Lembrando que preciso adiar minha execução pra que caso eu queira deletar algo no meu arquivo JSON, ele consiga e não
# o dump novamente com tudo igual. Como faço adio a execução de algo? Fazendo uma função daquilo


def fazerDump():
    with open(CAMINHO_ARQUIVO, 'w+') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
