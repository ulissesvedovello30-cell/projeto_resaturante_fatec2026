class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade, vendavel=True):
        self.__nome = nome
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda
        self.__data_compra = data_compra
        self.__data_vencimento = data_vencimento
        self.__quantidade = quantidade
        # vendavel=True: item pronto que aparece no cardápio (ex: Feijoada, Coca Cola)
        # vendavel=False: matéria-prima/ingrediente de estoque, não aparece pro cliente
        self.__vendavel = vendavel

    def is_vendavel(self):
        return self.__vendavel

    def get_nome(self):
        return self.__nome

    def get_preco_compra(self):
        return self.__preco_compra

    def get_preco_venda(self):
        return self.__preco_venda

    def get_data_compra(self):
        return self.__data_compra

    def get_data_vencimento(self):
        return self.__data_vencimento

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade