from datetime import datetime

STRUCTURE_DATE = "%Y-%m-%d"


class SimpleReport():
    @classmethod
    def date_structure(cls, date):
        return datetime.strptime(date, STRUCTURE_DATE)

    @classmethod
    def __old_manufacturing_date(cls, products):
        all_manufacturing_dates = []

        for product in products:
            all_manufacturing_dates.append(product["data_de_fabricacao"])

        result_data_manufacturing = min(all_manufacturing_dates)
        return result_data_manufacturing

    @classmethod
    def __closest_expiration_date(cls, products):
        all_expiration_dates = []
        today = datetime.today()

        for product in products:
            expiration_date = product["data_de_validade"]
            all_expiration_dates.append(
                SimpleReport.date_structure(expiration_date)
            )

        valid_date = SimpleReport.date_structure("9999-12-31")

        for value_date in all_expiration_dates:
            if value_date > today and value_date < valid_date:
                valid_date = value_date

        return valid_date.strftime(STRUCTURE_DATE)

    @classmethod
    def __more_products(cls, products):
        total_companies = []
        amount = 0
        result = ""

        for product in products:
            total_companies.append(product["nome_da_empresa"])

        for company in total_companies:
            if total_companies.count(company) > amount:
                amount = total_companies.count(company)
                result = company
        return result

    @staticmethod
    def generate(products):
        more_products = SimpleReport.__more_products(products)
        expiration_date = SimpleReport.__closest_expiration_date(products)
        data_manufacturing = SimpleReport.__old_manufacturing_date(products)

        return (
          f"Data de fabricação mais antiga: {data_manufacturing}\n"
          f"Data de validade mais próxima: {expiration_date}\n"
          f"Empresa com mais produtos: {more_products}"
        )
