import csv
import json
import os
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data_csv(cls, path):
        dict_products = []
        with open(path, mode='r') as file:
            read_file = csv.DictReader(file)
            for data in read_file:
                dict_products.append(data)
        return dict_products

    @classmethod
    def import_data_json(cls, path):
        dict_products = []
        with open(path, mode='r') as file:
            read_file = json.load(file)
            dict_products = read_file
        return dict_products

    @classmethod
    def import_data_xml(cls, path):
        dict_products = []
        with open(path, 'r') as file:
            file_xml = file.read()
            dict_products = xmltodict.parse(file_xml)
        return dict_products["dataset"]["record"]

    @classmethod
    def extension_valid(cls, path):
        data_file = []
        file, extension = os.path.splitext(path)
        if extension == ".csv":
            data_file = Inventory.import_data_csv(path)
        if extension == ".json":
            data_file = Inventory.import_data_json(path)
        if extension == ".xml":
            data_file = Inventory.import_data_xml(path)

        return data_file

    @staticmethod
    def import_data(path, str):
        products_file = Inventory.extension_valid(path)

        if str == "simples":
            return SimpleReport.generate(products_file)
        if str == "completo":
            return CompleteReport.generate(products_file)


print(Inventory.import_data("inventory_report/data/inventory.xml", "simples"))
