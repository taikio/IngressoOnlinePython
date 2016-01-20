import sqlite3


class PessoaDao():
    def __init__(self,pessoa):
        self.con = None
        self.cursor = None
        self.pessoa = pessoa

    def iniciaConexao(self):

        try:
            self.con = sqlite3.connect('ingressos.db')
            self.cursor = self.con.cursor()
            return
        except Exception:
            return

    def fechaConexao(self):

        try:
            self.cursor.close()
            self.con.close()
            return
        except Exception:
            return

    def cadastrar(self, nome, email, username, senha, nivelPermissao):

        self.iniciaConexao()

        try:
            sql = "INSERT INTO pessoa(nome,email,username,senha,nivel_permissao) " \
                "VALUES('"+nome+"','"+email+"','"+username+"','"+senha+"','"+nivelPermissao+"')"

            self.cursor.execute(sql)
            self.con.commit()

            self.fechaConexao()
            return True
        except Exception:
            return False

    def autenticar(self, username, senha):

        self.iniciaConexao()

        try:
            sql = 'SELECT * FROM pessoa'
            self.cursor.execute(sql)

            for registro in self.cursor.fetchall():
                if registro[3] == username and registro[4] == senha:
                    self.pessoa.username = registro[3]
                    self.pessoa.nivelPermissao = registro[5]

                    self.fechaConexao()
                    continue
            return True
        except Exception:
            return False










