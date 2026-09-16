class Node:
    # O node vai precisar apenas dos "dados" e o ponteiro para apontar para o proximo
    # a maioria das classes vão utilizar a classe Node
    def __init__(self,dados):
        self.__dados = dados
        self.__apontar_o_proximo = None

# Foi necessário criar esse geters e setters, pois a classe ListaEncadeada não iria conseguir
# usar os dados da classe Node sem quebrar a aplicação por causa do encapsulamento das variaveis.

    def get_dados(self):
        return self.__dados

    def set_dados(self, new_dados):
        self.__dados = new_dados

    def get_apontar_o_proximo(self):
        return self.__apontar_o_proximo

    def set_apontar_o_proximo(self, new_apontar_o_proximo):
        self.__apontar_o_proximo = new_apontar_o_proximo


