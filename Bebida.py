from enum import Enum

# conjunto fechado de bebidas válidas, usado na validação do Comanda.adicionar_item
class Bebida(Enum):
    COCA_COLA = "Coca Cola"
    SUCO = "Suco"
    AGUA = "Água"


# conjunto fechado de formas de pagamento aceitas na hora de fechar a conta
class FormaPagamento(Enum):
    DINHEIRO = "Dinheiro"
    CARTAO_CREDITO = "Cartão de Crédito"
    CARTAO_DEBITO = "Cartão de Débito"
    PIX = "Pix"