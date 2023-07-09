class Conn:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        conn = cls()
        conn.user = user
        conn.password = password
        return conn

    @staticmethod
    def log(pessoa):
        print(f'Log: {pessoa} entrou')


# A regra é assim: precisou da instância, usa o self
# Precisou da classe e seus componentes, usa @classmethod e cls
# Não precisa nem da instância, nem de nada? Usa o @staticmethod (ou cria uma função fora da classe né)

# Toda vez que preciso usar self, esse método é um método de instância
c1 = Conn()
c1.set_user('Luiz')  # O user será Luiz
print(c1.user)
auth = Conn.create_with_auth('Luiz', 'password')
print(auth.user,',', auth.password)
c1.log('Luiz')
