from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Celular",
        nome_da_empresa="Xaomi",
        data_de_fabricacao="22/08/2010",
        data_de_validade="10/11/2022",
        numero_de_serie="123456",
        instrucoes_de_armazenamento="livremente",
    )

    assert product.__repr__() == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
)
