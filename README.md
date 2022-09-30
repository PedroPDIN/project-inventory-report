# Boas-vindas ao repositório do Inventory Reports

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />

  Neste projeto foi utilizando de forma prática o conceito de  Programação Orientada a Objetos! foi implementado um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

  Esses dados de estoque poderão ser obtidos de diversas fontes:

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

  Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

  <strong>🚵 Habilidades que foram trabalhadas e práticas:</strong>
 

  <ul>
    <li>Aplicar conceitos de Orientação a Objetos em Python;</li>
    <li>Aplicar padrões de projeto;</li>
    <li>Leitura e escrita de arquivos (XML, CSV, JSON).</li>
  </ul>
</details>


<details>
  <summary><strong>Instalação do projeto</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:tryber/sd-016-a-inventory-report.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-016-a-inventory-report`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
</details>

<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />
  Três formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Confira o exemplo de formato eles:
  
  <strong>Arquivos CSV</strong>
  Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
[
  {
    "id":1,
    "nome_do_produto":"Borracha",
    "nome_da_empresa":"Papelaria Solar",
    "data_de_fabricacao":"2021-07-04",
    "data_de_validade":"2029-02-09",
    "numero_de_serie":"FR48",
    "instrucoes_de_armazenamento":"Ao abrigo de luz solar"
  }
]
```

<strong>Arquivos XML</strong>
Os arquivos **XML** seguem o seguinte modelo:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>Microfone</nome_do_produto>
    <nome_da_empresa>Tecno Uau LTDA</nome_da_empresa>
    <data_de_fabricacao>2021-10-27</data_de_fabricacao>
    <data_de_validade>2032-08-31</data_de_validade>
    <numero_de_serie>MT08</numero_de_serie>
    <instrucoes_de_armazenamento>Longe de fonte de calor</instrucoes_de_armazenamento>
  </record>
</dataset>
```
</details>



# Requisitos 

## 1 - Testar o construtor/inicializador do objeto Produto
> **Teste Criando em:** tests/product/test_product.py

  <p align="center">
    <img src="/.images/construtor.png " alt="Imagem de construtor em Python"  width="600"/>
  </p>

arquivo: `inventory_report/inventory/product.py`, a classe **Product**.

Verificar se o método `__init__` da classe Product esta funcionando corretamente.

O nome do test `test_cria_produto`, ele deve verificar o correto preenchimento dos seguintes atributos:
  - id (int)
  - nome_da_empresa (string)
  - nome_do_produto (string)
  - data_de_fabricacao (string)
  - data_de_validade (string)
  - numero_de_serie (string)
  - instrucoes_de_armazenamento (string)


## 2 - Testar o relatório individual do produto
> **Teste criado em:** tests/product_report/test_product_report.py

Boa novidade, o primeiro relatório já implementado pela _TRYBE_ neste arquivo `inventory_report/inventory/product.py`. Formulando por tanto em  uma frase construída com as informações do produto, que será muito útil para etiquetar o estoque.

Para desenvolver este relatório, foi utilizado o recurso `__repr__` do Python, que permite alterar a representatividade do objeto, para que sempre que usarmos um print nele, no lugar de endereço de memória, teremos uma String personalizada. 

**Dica:** A reimplementação do `__repr__` não faz o objeto retornar exatamente uma `string`, com isso foi necessário fazer um `cast` para `string`.

Exemplo da frase:
> O produto `farinha` fabricado em `01-05-2021` por `Farinini` com validade até `02-06-2023` precisa ser armazenado `ao abrigo de luz`.

O nome do teste `test_relatorio_produto`, ele deve instanciar um objeto `Product` e verificar se acessá-lo a frase de retorno esta correta.

## 3 - Gerar a versão simplificada do relatório

> **A classe fica localizada em:** inventory_report/reports/simple_report.py

O relatório é gerado através de um método de classe chamado `generate` escrito dentro da classe `SimpleReport`.

- O método recebe um parâmetro que representa uma `list` (estrutura de dados), onde cada posição contém um `dict`(estrutura de dados).

Exemplo de formato de entrada

```json
   [
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
   ]
```

- O método retorna uma `string` de saída com o seguinte formato:
   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com mais produtos: NOME DA EMPRESA
   ```
- A data de validade mais próxima, somente considera itens que ainda não venceram.

## 4 - Gerar a versão completa do relatório

> **Localizada em:** inventory_report/reports/complete_report.py

O relatório é gerado através de um método `generate` para a classe `CompleteReport`.
Ele recebe dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório.
  
- O método recebe de parâmetro uma lista de dicionários no seguinte **formato**:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "MESA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-05-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
     }
   ]
   ```

- O método retorna uma saída com o seguinte formato:

```bash
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```

## 5 - Relatórios através de um arquivo CSV
> **Localizado em:** inventory_report/inventory/inventory.py

O método recebe como primeiro parâmetro uma string como caminho para o arquivo `CSV` e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - **3** - Ao importar um arquivo CSV, deve retornar o relatórios simples ou o completo conforme solicitado.

</details>

## 6 - Gere os relatórios através de um arquivo JSON
> **Incremente em:** `inventory_report/inventory/inventory.py`. 

> 📌 Utilize o mesmo método do requisito anterior.

Altere o método `import_data` para que ele também seja capaz de carregar arquivos `JSON`.
    
Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, ele recupera os dados do arquivo e chama o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` chama o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

## 7 - Relatórios através de um arquivo XML
> **Localizado em:** `inventory_report/inventory/inventory.py`. 
    
O método recebe como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, ele recupera os dados do arquivo e chama o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

#### :warning: Importante :warning:: O grupo Trybe foi responsável por realizar o inicio do projeto (e também os commits iniciais), mas precisamente a estrutura do projeto e as configuração dos tests para a avaliação do projeto.