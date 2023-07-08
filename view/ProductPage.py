import re
import time
import allure
from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from objects.Locator import Locator
from view.MainPage import MainPage


class Locators:
    FILTER = Locator(
        By.XPATH, "//div[contains(@class,'facet')]//*[contains(text(),'{name}')]")
    FILTER_MENU = Locator(By.CSS_SELECTOR, ".facet__menu-content")
    SEARCH_FIELD = Locator(By.CSS_SELECTOR, "[name='facet-search']")
    SEARCH_OPTION = Locator(
        By.XPATH, "//div[contains(@class,'facet-option')]//div[text()[contains(., '{name}')]]")
    SELECT_SEARCH_OPTION = Locator(By.XPATH,
                                   SEARCH_OPTION.locator + "/../..//*[@class='facet-option__checkbox']")
    SELECT_SEARCH_OPTION_SELECTED = Locator(By.XPATH,
                                            SEARCH_OPTION.locator + "/../..//*[contains(@class,'facet-option__checkbox--selected')]")
    CONFIRM_SEARCH = Locator(
        By.CSS_SELECTOR, FILTER_MENU.locator + " button[class*=close-button]")
    FILTER_BUTTON = Locator(By.XPATH, "//button[text()='Filter']")
    TOTAL_PRODUCTS = Locator(
        By.CSS_SELECTOR, "div.product-overview__headline-wrapper")
    PRODUCT = Locator(By.CSS_SELECTOR, "div.product-grid-column")
    SEARCH_PAGE = Locator(
        By.CSS_SELECTOR, "[data-testid='pagination-title-dropdown']")
    PRODUCT_NAME = Locator(
        By.CSS_SELECTOR, PRODUCT.locator + " .product-info .name")
    PRODUCT_PRICE = Locator(
        By.CSS_SELECTOR, PRODUCT.locator + " .product-info .price-row")
    NEWSLETTER_FOOTER = Locator(By.CSS_SELECTOR, ".newsletter-footer")


class ProductPage(MainPage):
    """
    Class with the actions that need to be done into the product page
    """

    def __init__(self, driver: WebDriver):
        """
        Constructor of the page
        :param driver: Selenium WebDriver
        """
        super().__init__(driver)
        self.page_url += "/c/parfum/01"

    def visit(self, extra_path: str = ""):
        """
        Visit the page and wait for elements to load
        """
        super().visit(extra_path)
        self.wait_for(Locators.SEARCH_PAGE())

    @allure.step("Select {fields} in {filter_name}")
    def filter_for(self, filter_name: str, fields: List[str]):
        """
        Apply a filter to the showing products
        :param filter_name: The name of the filter to apply
        :param fields: The selection/s to apply in the filter
        """
        with allure.step(f"Selecting {filter_name}"):
            self.wait_for_clickable(Locators.FILTER(name=filter_name)).click()
            if not self.find_if_present(Locators.FILTER_MENU()):
                time.sleep(1)
                print("Warning filter did not open")
                self.wait_for_clickable(
                    Locators.FILTER(name=filter_name)).click()
            self.wait_for(Locators.CONFIRM_SEARCH())
        for field in fields:
            with allure.step(f"Selecting {field} field"):
                search_bar = self.find_if_present(Locators.SEARCH_FIELD())
                if search_bar:
                    search_bar = self.wait_for_clickable(
                        Locators.SEARCH_FIELD())
                    search_bar.send_keys(field)
                self.wait_for_clickable(
                    Locators.SELECT_SEARCH_OPTION(name=field)).click()
                self.wait_for(
                    Locators.SELECT_SEARCH_OPTION_SELECTED(name=field))
                if search_bar:
                    search_bar.clear()

        with allure.step("Confirming the filter selection"):
            self.wait_for_clickable(Locators.CONFIRM_SEARCH()).click()
            self.wait_not_present(Locators.FILTER_MENU())

    def product_count(self) -> str:
        """
        Get the total number of products that satisfy the filters
        """
        text = self.find(Locators.TOTAL_PRODUCTS()).text
        return re.search(r"\(([\d\.]+?)\)", text).group(1)
