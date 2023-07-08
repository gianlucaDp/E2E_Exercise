import pytest
from view.MainPage import MainPage
from view.ProductPage import ProductPage


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)
