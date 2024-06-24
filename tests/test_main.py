import pytest

from src.classes import Category, Product


@pytest.fixture
def smartphone():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


def test_init(smartphone):
    assert smartphone.name == 'Samsung Galaxy C23 Ultra'
    assert smartphone.description == '256GB, Серый цвет, 200MP камера'
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5


@pytest.fixture
def category_smartphone():
    return Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение '
                                 'дополнительных функций для удобства жизни', Product)


def test_init(category_smartphone):
    assert category_smartphone.name == 'Смартфоны'
    assert category_smartphone.description == ('Смартфоны, как средство не только коммуникации, но и получение '
                                               'дополнительных функций для удобства жизни')
    assert category_smartphone.product == Product
