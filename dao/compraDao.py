import sqlite3


class CompraDao():

    def __init__(self):
        self.con = None
        self.cursor = None

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

    def cadastrar(self,nomeIngresso, tipoIngresso, quantidade,valorUnit,valorTotal,comprador):

        self.iniciaConexao()

        try:
            sql = "INSERT INTO compra(nome_ingresso,tipo_ingresso,quantidade,valor_unitario,valor_total,comprador)"\
                  "VALUES('"+nomeIngresso+"','"+tipoIngresso+"',"+str(quantidade)+","+str(valorUnit)+","+str(valorTotal)+",'"+comprador+"')"

            self.cursor.execute(sql)
            self.con.commit()

            self.fechaConexao()
            return True
        except Exception:
            return False

    def retornarPorUsuario(self,comprador,compra):

        self.iniciaConexao()
        lista = list()

        try:
            sql = 'SELECT * FROM compra'
            self.cursor.execute(sql)

            for registro in self.cursor.fetchall():
                if registro[6] == comprador:
                    compra.nomeIngresso = registro[1]
                    compra.tipoIngresso = registro[2]
                    compra.quantidade = registro[3]
                    compra.valorUnit = registro[4]
                    compra.valorTotal = registro[5]
                    compra.comprador = registro[6]
                    lista.append(compra)

            return lista
        except:
            return

