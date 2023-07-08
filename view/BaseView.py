import os
import time
import allure
from typing import Tuple, List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseView:
    """
    Class with basic actions that apply to all pages
    ...
    Attributes
    ----------
    driver : WebDriver
         WebDriver that will be used to automate the test
    wait : WebDriverWait
        Default wait of the driver, can be used when waiting for elements
    """

    def __init__(self, driver: WebDriver, wait: int = 20):
        """
        Constructor of the base view
        :param driver: Selenium WebDriver
        :param wait: How long the driver should wait for an element to appear / to try to interact
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait)
        self.page_url = os.getenv("BASE_URL", "")

    def visit(self, extra_path: str = ""):
        """
        Visit the page url
        :param extra_path: optional extra endpoint to add to the page url
        """
        with allure.step(f"Visiting {self.page_url + extra_path}"):
            self.driver.get(self.page_url + extra_path)
            time.sleep(0.5)

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """
        Find an element in the page
        :param locator: tuple containing the locator type and string
        :return: WebElement if found, otherwise a NoSuchElementException is raised
        """
        return self.driver.find_element(*locator)

    def find_if_present(self, locator: Tuple[str, str]) -> WebElement:
        """
        Find an element in the page
        :param locator: tuple containing the locator type and string
        :return: Element if found, otherwise None
        """
        elements = self.driver.find_elements(*locator)
        return elements[0] if elements else None

    def find_multiple(self, locator: Tuple[str, str]) -> List[WebElement]:
        """
        Find multiple elements in the page
        :param locator: tuple containing the locator type and string
        :return: List of founds element, can be empty if no element found
        """
        return self.driver.find_elements(*locator)

    def wait_for(self, locator: Tuple[str, str]) -> WebElement:
        """
        Wait for an element in the page
        :param locator: tuple containing the locator type and string
        :return: Element if found before timeout, otherwise a TimeoutException is raised
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element

    def wait_for_clickable(self, locator: Tuple[str, str]) -> WebElement:
        """
        Wait for an element in the page to be clickable
        :param locator: tuple containing the locator type and string
        :return: Element if found before timeout, otherwise a TimeoutException is raised
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element

    def wait_not_present(self, locator):
        """
        Wait for an element to not be present in the page
        :param locator: tuple containing the locator type and string
        :raises: A TimeoutException is raised if the element is still present after the timeout
        """
        self.wait.until(EC.invisibility_of_element_located(locator))

    def is_current_page(self):
        """
        Verify if the current page in the driver is equal to the class page_url
        """
        with allure.step(f"Verify the current url is {self.page_url}"):
            EC.url_matches(self.page_url)
