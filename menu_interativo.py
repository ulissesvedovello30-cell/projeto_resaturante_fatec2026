from comanda import Comanda
from gerenciadorComandas import GerenciadorComandas
from Produto import Produto
from Fila import Fila
from popular_dados import gerar_comandas_aleatorias, gerar_estoque_aleatorio
from persistencia import salvar_dados, carregar_dados

gerenciador = GerenciadorComandas()
estoque = Fila()

# esse menu interativo é para garçons e gerente do restaurante para abrir ou fechar comandas
# e controle de estoque do restaurante
while True:
    print("\n--- MENU ---")
    print("1 - Abrir comanda")
    print("2 - Adicionar item a uma comanda")
    print("3 - Remover item de uma comanda")
    print("4 - Mostrar uma comanda")
    print("5 - Fechar comanda")
    print("6 - Adicionar produto ao estoque")
    print("7 - Editar quantidade de estoque")
    print("8 - Listar estoque")
    print("9 - Popular com dados aleatorios (Faker)")
    print("10 - Salvar dados em arquivo (pickle)")
    print("11 - Carregar dados de arquivo (pickle)")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Número da comanda: "))
        nome = input("Nome do cliente: ")
        data_hora = input("Data/hora de abertura: ")
        gerenciador.abrir_comanda(Comanda(numero, nome, data_hora))
        print("Comanda aberta com sucesso.")

    elif opcao == "2":
        comanda = gerenciador.buscar_comanda(int(input("Número da comanda: ")))
        if comanda is None:
            print("Comanda não encontrada.")
        else:
            dado = input("Nome do item: ")
            tipo = input("Tipo (refeicoes/bebidas): ")
            comanda.adicionar_item(dado, tipo)

    elif opcao == "3":
        comanda = gerenciador.buscar_comanda(int(input("Número da comanda: ")))
        if comanda is None:
            print("Comanda não encontrada.")
        else:
            dado = input("Nome do item a remover: ")
            tipo = input("Tipo (refeicoes/bebidas): ")
            comanda.remover_item(dado, tipo)

    elif opcao == "4":
        comanda = gerenciador.buscar_comanda(int(input("Número da comanda: ")))
        if comanda is None:
            print("Comanda não encontrada.")
        else:
            comanda.mostrar()

    elif opcao == "5":
        comanda = gerenciador.buscar_comanda(int(input("Número da comanda: ")))
        if comanda is None:
            print("Comanda não encontrada.")
        else:
            gerenciador.fechar_comanda(comanda)
            print("Comanda fechada.")

    elif opcao == "6":
        nome = input("Nome do produto: ")
        preco_compra = int(input("Preço de compra: "))
        preco_venda = float(input("Preço de venda: "))
        data_compra = input("Data de compra: ")
        data_vencimento = input("Data de vencimento: ")
        quantidade = int(input("Quantidade: "))
        estoque.enfileirar(Produto(nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade))
        print("Produto adicionado ao estoque.")

    elif opcao == "7":
        nome_produto = input("Nome do produto: ")
        nova_quantidade = int(input("Nova quantidade: "))
        estoque.editar_quantidade(nome_produto, nova_quantidade)

    elif opcao == "8":
        estoque.listar()

    elif opcao == "9":
        qtd_comandas = int(input("Quantas comandas gerar: "))
        qtd_produtos = int(input("Quantos produtos gerar: "))
        gerar_comandas_aleatorias(gerenciador, qtd_comandas)
        gerar_estoque_aleatorio(estoque, qtd_produtos)
        print("Dados aleatorios gerados com sucesso.")

    elif opcao == "10":
        salvar_dados(gerenciador, estoque)
        print("Dados salvos em dados_restaurante.pkl")

    elif opcao == "11":
        gerenciador, estoque = carregar_dados()
        print("Dados carregados com sucesso.")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")