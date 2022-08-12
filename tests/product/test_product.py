from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Celular",
        nome_da_empresa="Xaomi",
        data_de_fabricacao="22/08/2010",
        data_de_validade="10/11/2022",
        numero_de_serie="123456",
        instrucoes_de_armazenamento="livremente",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Celular"
    assert product.nome_da_empresa == "Xaomi"
    assert product.data_de_fabricacao == "22/08/2010"
    assert product.data_de_validade == "10/11/2022"
    assert product.numero_de_serie == "123456"
    assert product.instrucoes_de_armazenamento == "livremente"
