from ListaEncadeada import ListaEncadeada
class Comanda:
    def __init__(self,numero,nome,data_hora):
        self.__numero_comanda = numero
        self.__nome_cliente = nome
        self.__data_hora_pedido = data_hora
        self.__refeicoes = ListaEncadeada()# tipo 1
        self.__bebidas = ListaEncadeada()# tipo 2

    def adicionar_item(self,dado,tipo):
        if tipo == "refeicoes": # tipo 1
            self.__refeicoes.inserir(dado)
        elif tipo == "bebidas": # tipo 2
            self.__bebidas.inserir(dado)

    def remover_item(self,dado,tipo):
        if tipo == "refeicoes":
            self.__refeicoes.remover(dado)
        elif tipo == "bebidas":
            self.__bebidas.remover(dado)
