from ListaEncadeada import ListaEncadeada
from Bebida import Bebida
class Comanda:
    def __init__(self,numero,nome,data_hora):
        self.__numero_comanda = numero
        self.__nome_cliente = nome
        self.__data_hora_pedido = data_hora
        self.__refeicoes = ListaEncadeada()# tipo 1
        self.__bebidas = ListaEncadeada()# tipo 2

# Esse def serve para mostrar que os dados foram realmente colocados dentro da comanda
    def mostrar(self):
        print(f"Comanda {self.__numero_comanda} - Cliente: {self.__nome_cliente}")
        print(f"Data e hora da abertura: {self.__data_hora_pedido}")
        print("Refeições:")
        self.__refeicoes.listar()
        print("Bebidas:")
        self.__bebidas.listar()

    def adicionar_item(self, dado, tipo):
        if tipo == "refeicoes":
            self.__refeicoes.inserir(dado)
        elif tipo == "bebidas":
            # bebida só pode ser uma das opções do Enum (Coca Cola, Suco ou Água)
            valores_validos = [b.value for b in Bebida]
            if dado in valores_validos:
                self.__bebidas.inserir(dado)
            else:
                print(f"{dado} não está disponível no estoque.")

    def remover_item(self, dado, tipo):
        if tipo == "refeicoes":
            self.__refeicoes.remover(dado)
        elif tipo == "bebidas":
            self.__bebidas.remover(dado)

# get de busca da comanda
    def get_numero(self):
        return self.__numero_comanda