# -*- coding: utf-8 -*-
import sqlite3

class DaoHelper():

    def __init__(self):
        self.con = None
        self.cursor = None


    def criarTabelas(self):
        self.con = sqlite3.connect('ingressos.db')
        self.cursor = self.con.cursor()

        sqlPessoa = """ CREATE TABLE IF NOT EXISTS pessoa
              (id integer primary key autoincrement,
              nome varchar(200),
              email varchar(200),
              username varchar(10),
              senha varchar(10),
              nivel_permissao varchar(20))"""

        self.cursor.execute(sqlPessoa)

        sqlIngresso = """ CREATE TABLE IF NOT EXISTS ingresso
                      (id integer primary key autoincrement,
                       nome varchar(200),
                       categoria varchar(200),
                       valor real,
                       quantidade integer); """

        self.cursor.execute(sqlIngresso)

        sqlCompra = """ CRATE TABLE IF NOT EXISTS compra
                        (id integer primary key autoincrement,
                        nome_ingresso varchar(200),
                        tipo_ingresso varchar(200),
                        valor_unitario """