import pickle

# pickle transforma os objetos Python (gerenciador + estoque) em bytes e grava num arquivo,
# assim os dados sobrevivem depois que o programa fecha (armazenamento não volátil)

def salvar_dados(gerenciador, estoque, cardapio_pratos, caminho="dados_restaurante.pkl"):
    with open(caminho, "wb") as arquivo:
        pickle.dump((gerenciador, estoque, cardapio_pratos), arquivo)


def carregar_dados(caminho="dados_restaurante.pkl"):
    # devolve a mesma tupla (gerenciador, estoque, cardapio_pratos) salva antes, reconstruída do arquivo
    with open(caminho, "rb") as arquivo:
        return pickle.load(arquivo)
