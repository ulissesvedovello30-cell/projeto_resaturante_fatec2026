from enum import Enum

# conjunto fechado de bebidas válidas, usado na validação do Comanda.adicionar_item
class Bebida(Enum):
    COCA_COLA = "Coca Cola"
    SUCO = "Suco"
    AGUA = "Água"