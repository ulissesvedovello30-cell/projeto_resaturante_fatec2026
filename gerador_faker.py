from faker import Faker
from comanda import Comanda
from Produto import Produto
from Bebida import Bebida

# Faker gera dados fake (nomes, datas, palavras) só pra popular o sistema de teste
fake = Faker("pt_BR")

REFEICOES_DISPONIVEIS = ["Feijoada", "Picanha", "Lasanha", "Salada Caesar", "Frango Grelhado"]


def gerar_comandas_aleatorias(gerenciador, quantidade):
    # cria N comandas com cliente, refeição e bebida aleatórios, e já abre no gerenciador
    for numero in range(1, quantidade + 1):
        nome_cliente = fake.name()
        data_hora = fake.date_time_this_year().strftime("%d/%m/%Y %H:%M")
        comanda = Comanda(numero, nome_cliente, data_hora)

        refeicao_aleatoria = fake.random_element(REFEICOES_DISPONIVEIS)
        bebida_aleatoria = fake.random_element([b.value for b in Bebida])
        comanda.adicionar_item(refeicao_aleatoria, "refeicoes")
        comanda.adicionar_item(bebida_aleatoria, "bebidas")

        gerenciador.abrir_comanda(comanda)


def popular_cardapio_fixo(estoque):
    # cardápio fixo com preço real, pra não precisar cadastrar produto na mão na demo
    cardapio = [
        ("Feijoada", 15.0, 35.0),
        ("Picanha", 25.0, 55.0),
        ("Lasanha", 12.0, 28.0),
        ("Salada Caesar", 8.0, 20.0),
        ("Frango Grelhado", 10.0, 24.0),
        ("Coca Cola", 3.0, 7.0),
        ("Suco", 2.5, 6.0),
        ("Água", 1.5, 4.0),
    ]
    for nome, preco_compra, preco_venda in cardapio:
        produto = Produto(nome, preco_compra, preco_venda, "01/09/2026", "01/03/2027", 50)
        estoque.enfileirar(produto)


def gerar_estoque_aleatorio(estoque, quantidade):
    # cria N produtos aleatórios e enfileira no estoque (Fila)
    for _ in range(quantidade):
        nome_produto = fake.word().capitalize()
        preco_compra = round(fake.pyfloat(min_value=1, max_value=20, right_digits=2), 2)
        preco_venda = round(preco_compra * 2, 2)
        data_compra = fake.date_this_year().strftime("%d/%m/%Y")
        data_vencimento = fake.date_this_decade().strftime("%d/%m/%Y")
        quantidade_estoque = fake.random_int(min=5, max=100)

        produto = Produto(nome_produto, preco_compra, preco_venda, data_compra, data_vencimento, quantidade_estoque)
        estoque.enfileirar(produto)
