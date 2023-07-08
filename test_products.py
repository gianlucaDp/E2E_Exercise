
import pytest
from view.MainPage import MainPage
from view.ProductPage import ProductPage
import allure


@pytest.fixture(scope="session", autouse=True)
def accept_cookies(driver):
    main_page = MainPage(driver)
    main_page.visit()
    main_page.accept_cookies()


@allure.title("Visit Perfumes section")
@allure.description("""The user can visit the perfumes search page by opening the PARFUM section""")
def test_first_visit_perfumes(main_page: MainPage, product_page: ProductPage):
    main_page.visit()
    main_page.open_section("PARFUM")
    product_page.is_current_page()


@allure.title("Filter the available perfumes")
@allure.description("""The user can select different filters to narrow the showed products""")
def test_filter_perfumes(filter_data, product_page: ProductPage):
    (filters, expected_products) = filter_data
    product_page.visit()
    for filter_name, filter_values in filters.items():
        product_page.filter_for(filter_name, filter_values)
    products_after = product_page.product_count()
    with allure.step("Check filter is applied"):
        assert str(products_after) == str(expected_products)


@allure.title("Failing test")
@allure.description("""Test that fails to show the screenshot in the report""")
def test_fail_example(main_page: MainPage):
    main_page.visit()
    assert False, "Fail the test"
