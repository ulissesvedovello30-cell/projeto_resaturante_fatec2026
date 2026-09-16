from ListaEncadeada import ListaEncadeada

class GerenciadorComandas:
    # guarda todas as comandas abertas do restaurante, reaproveitando a ListaEncadeada
    def __init__(self):
        self.__comandas_abertas = ListaEncadeada()

    def abrir_comanda(self, comanda):
        self.__comandas_abertas.inserir(comanda)

    def fechar_comanda(self, comanda):
        self.__comandas_abertas.remover(comanda)

    def listar_comandas(self):
        self.__comandas_abertas.listar()

    def buscar_comanda(self, numero):
        return self.__comandas_abertas.buscar(lambda c: c.get_numero() == numero)