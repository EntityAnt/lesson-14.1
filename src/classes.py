class Product:
    """ Класс для описания товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity




class Category:
    """ Класс для описания категории товаров"""
    category_count = 0
    products = 0

    def __init__(self, name: str, description: str, product: Product):
        self.name = name
        self.description = description
        self.product = product
        Category.category_count += 1
        Category.products += 1


