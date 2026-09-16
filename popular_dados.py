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
