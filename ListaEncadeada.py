from Node import Node
class ListaEncadeada:
    def __init__(self):
        self.__head = None


    def inserir(self, dado):
        # lista vazia: o novo nó vira o head direto
        if self.__head is None:
            self.__head = Node(dado)
        else:
            # percorre até achar o último nó (o que aponta para None) e conecta o novo nó nele
            atual = self.__head
            while atual.get_apontar_o_proximo() is not None:
                atual = atual.get_apontar_o_proximo()
            atual.set_apontar_o_proximo(Node(dado))

    def remover(self, dado):
        if self.__head is None:
            return
        elif self.__head.get_dados() == dado:
            # o item procurado é o próprio head: só pula pro próximo
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
        # imprime o dado de cada nó, do head até o fim
        atual = self.__head
        while atual is not None:
            print(atual.get_dados())
            atual = atual.get_apontar_o_proximo()

    def obter_todos(self):
        # devolve os dados da lista como uma lista comum, só pra facilitar somas
        itens = []
        atual = self.__head
        while atual is not None:
            itens.append(atual.get_dados())
            atual = atual.get_apontar_o_proximo()
        return itens

    def buscar(self, condicao):
        # condicao é uma função que recebe um dado e devolve True/False;
        # devolve o primeiro dado que bate com a condição, ou None se não achar
        atual = self.__head
        while atual is not None:
            if condicao(atual.get_dados()):
                return atual.get_dados()
            atual = atual.get_apontar_o_proximo()
        return None
