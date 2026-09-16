from Node import Node
class ListaEncadeada:
    def __init__(self):
        self.__head = None


    def inserir(self, dado):
        if self.__head is None:
            self.__head = Node(dado)
        else:
            atual = self.__head
            while atual.get_apontar_o_proximo() is not None:
                atual = atual.get_apontar_o_proximo()
            atual.set_apontar_o_proximo(Node(dado))

    def remover(self, dado):
        if self.__head is None:
            return
        elif self.__head.get_dados() == dado:
            self.__head = self.__head.get_apontar_o_proximo()
        else:
            anterior = self.__head
            atual = self.__head.get_apontar_o_proximo()
            while atual is not None:
                if atual.get_dados() == dado:
                    anterior.set_apontar_o_proximo(atual.get_apontar_o_proximo())
                    return
                anterior = atual
                atual = atual.get_apontar_o_proximo()


    def listar(self):
        atual = self.__head
        while atual is not None:
            print(atual.get_dados())
            atual = atual.get_apontar_o_proximo()