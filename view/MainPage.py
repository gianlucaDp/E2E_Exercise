import time
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from objects.Locator import Locator
from view.BaseView import BaseView
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    ACCEPT_COOKIES = Locator(
        By.CSS_SELECTOR, "button.uc-list-button__accept-all")
    SECTION = Locator(
        By.XPATH, "//div[contains(@class,'header-component')]//a[contains(text(),'{name}')]")


class MainPage(BaseView):
    """
    Class with the actions that need to be done into the main page
    """

    def __init__(self, driver: WebDriver):
        """
        Constructor of the page
        :param driver: Selenium WebDriver
        """
        super().__init__(driver)

    @allure.step("Accept the cookies")
    def accept_cookies(self):
        """
        Accept the cookies popup, clicking on confirm
        """
        self.wait_for(Locators.ACCEPT_COOKIES()).click()
        self.wait_for_clickable(Locators.SECTION(name=""))
        time.sleep(1)

    @allure.step("Opening the {section_name} section")
    def open_section(self, section_name):
        """
        Open one of the sections of the website, available in the upper menu
        :param section_name: Name of the section to open
        """
        self.wait_for(Locators.SECTION(name=section_name)).click()
