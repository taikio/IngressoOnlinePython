from dao import pessoaDao


class Pessoa():

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.email = ''
        self.username = ''
        self.senha = ''
        self.nivelPermissao = ''
        self.dao = pessoaDao.PessoaDao(self)

    def cadastrar(self, nome, email, username, senha):
        self.nome = nome
        self.email = email
        self.username = username
        self.senha = senha
        self.nivelPermissao = 'admin'

        if self.dao.cadastrar(self.nome,self.email,self.username,self.senha,self.nivelPermissao):
            return True

        return False

    def autenticar(self, username, senha):

        if self.dao.autenticar(username, senha):
            return True

        return False