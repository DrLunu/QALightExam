from pages.base_page import BasePage
from pages.header_bar import HeaderBar


class StartPageConstants:
    """Stores constants for Start Page"""

    TOP_PRODUCTS_LINK_XPATH = './/div[@class="section-headline"]//a[@href="https://darijewelry.com/topovi-prykrasy"]'


class StartPage(BasePage):
    """Representation of Start Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants
        self.header_bar = HeaderBar(self.driver)

    def is_start_page(self):
        """Returns True if current page is Start Page"""

        return self.is_element_presence(self.constants.TOP_PRODUCTS_LINK_XPATH)
