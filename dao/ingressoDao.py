# -*- coding: utf-8 -*-
import sqlite3


class IngressoDao():

    def __init__(self):
        self.con = None
        self.cursor = None

    def iniciaConexao(self):
        self.con = sqlite3.connect('ingressos.db')
        self.cursor = self.con.cursor()

    def fechaConexao(self):
        self.cursor.close()
        self.con.close()

    def cadastrar(self,nome, tipo, valor, quantidade):

        self.iniciaConexao()

        try:
            sql = "INSERT INTO ingresso(nome,categoria,valor,quantidade) VALUES" \
                       "(' "+nome+" ',' "+tipo+" ',"+valor+","+quantidade+"); "

            self.cursor.execute(sql)
            self.con.commit()
            return
        except IOError:
            return

    def retornarTodos(self,ingresso):

        self.iniciaConexao()
        lista = list()

        try:
            sql = 'SELECT * FROM ingresso'
            self.cursor.execute(sql)

            for registro in self.cursor.fetchall():

                ingresso.nome = registro[1]
                ingresso.tipoIngresso = registro[2]
                ingresso.valor = registro[3]
                ingresso.quantidade = registro[4]

                print(ingresso.nome)
                lista.append(ingresso)




            for i in lista:
                print("-------")
                print(i.nome)

            return lista
        except:
            return