class node:
    # O node vai precisar apenas dos "dados" e o ponteiro para apontar para o proximo
    # a maioria das classes vão utilizar a classe Node
    def __init__(self,dados):
        self.__dados = dados
        self.__apontar_o_proximo = None
