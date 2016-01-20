from dao import ingressoDao

class Ingresso():

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.tipoIngresso = ''
        self.valor = 0.00
        self.quantidade = 0
        self.dao = ingressoDao.IngressoDao()

    def cadastrar(self, nome, tipoIngresso, valor, quantidade):

        self.dao.cadastrar(nome, tipoIngresso, valor, quantidade)

        return

    def retornarTodos(self):

        lista = list()
        lista = self.dao.retornarTodos(self)

        return lista