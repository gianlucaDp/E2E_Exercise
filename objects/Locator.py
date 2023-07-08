from typing import Tuple


class Locator:
    """
    A container for the locators needed to find elements in a page.
    Before using a locator the object must be called.
    ...
    Attributes
    ----------
    locator_type : str
        Type of the locator
    locator : str
        string representation of the locator, can be before formatting
    """

    def __init__(self, locator_type: str, locator_string: str):
        """
        Costructor of the class
        :param locator_type: Type of the locator
        :param locator_string: string representation of the locator
        """
        self.locator_type = locator_type
        self.locator = locator_string

    def __call__(self, **kwargs) -> Tuple[str, str]:
        """
        Returns the locator tuple that can be used into Selenium functions
        :param kwargs: If present it will try to format the locator string before returning the object
        :return: tuple containing the type of the locator and the final string representation of the locator
        """
        locator = self.locator.format(**kwargs) if kwargs else self.locator
        return self.locator_type, locator
