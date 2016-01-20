from dao import compraDao


class Compra():

    def __init__(self):
        self.id = None
        self.nomeIngresso = None
        self.tipoIngresso = None
        self.quantidade = None
        self.valorUnit = None
        self.valorTotal = None
        self.comprador = None
        self.dao = compraDao.CompraDao()

    def cadastrar(self, nomeIngresso, tipoIngresso, quantidade,valorUnit,valorTotal,comprador):

       if self.dao.cadastrar(nomeIngresso, tipoIngresso, quantidade,valorUnit,valorTotal,comprador):
           return True

       return False

    def retornarPorUsuario(self,comprador):

        lista = self.dao.retornarPorUsuario(comprador,self)

        return lista
