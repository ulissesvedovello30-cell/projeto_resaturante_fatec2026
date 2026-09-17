from Node import Node

class Fila:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def enfileirar(self, dado):
        # entra sempre pelo final (tail), preservando a ordem de chegada
        novo_no = Node(dado)
        if self.__head is None:
            self.__head = novo_no
            self.__tail = novo_no
        else:
            self.__tail.set_apontar_o_proximo(novo_no)
            self.__tail = novo_no

    def desenfileirar(self):
        # sai sempre pelo head (o mais antigo) -> regra FIFO,
        # garante que o produto mais velho seja usado primeiro
        if self.__head is None:
            return None
        removido = self.__head.get_dados()
        self.__head = self.__head.get_apontar_o_proximo()
        return removido

    def listar(self):
        atual = self.__head
        while atual is not None:
            print(atual.get_dados().get_nome())
            atual = atual.get_apontar_o_proximo()

    def get_preco(self, nome_produto):
        # busca o preço de venda de um produto pelo nome, usado no fechamento da conta
        atual = self.__head
        while atual is not None:
            if atual.get_dados().get_nome() == nome_produto:
                return atual.get_dados().get_preco_venda()
            atual = atual.get_apontar_o_proximo()
        return 0

    def editar_quantidade(self, nome_produto, nova_quantidade):
        atual = self.__head
        while atual is not None:
            if atual.get_dados().get_nome() == nome_produto:
                atual.get_dados().set_quantidade(nova_quantidade)
                return
            atual = atual.get_apontar_o_proximo()