import json
import os.path

from src.classes import Product


def main() -> None:
    path = os.path.join(os.getcwd(), 'data', 'products.json')
    with open(path, encoding='utf-8') as file:
        json_data = json.load(file)

    categories = []
    products = []

    for item in json_data:
        for product in item.get('products'):
            name = product.get('name', '')
            description = product.get('description', '')
            price = product.get('price', 0)
            quantity = product.get('quantity', 0)
            products.append(Product(name, description, price, quantity))

    print(products)


if __name__ == '__main__':
    main()
