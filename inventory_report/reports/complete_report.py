from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def __quantity_products(cls, products):
        all_total_companies = []
        companies = {}
        result = ""

        for product in products:
            all_total_companies.append(product["nome_da_empresa"])

        for company in all_total_companies:
            if company not in companies:
                companies[company] = 0
            companies[company] += 1

        for company in companies.items():
            result += f"- {company[0]}: {company[1]}\n"

        return result

    @staticmethod
    def generate(products):
        simple_report = SimpleReport.generate(products)
        quantity_products = CompleteReport.__quantity_products(products)

        return (
          f"{simple_report}\n"
          "Produtos estocados por empresa:\n"
          f"{quantity_products}"
        )
