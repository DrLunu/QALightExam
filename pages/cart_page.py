from pages.base_page import BasePage
from pages.header_bar import HeaderBar


class CartConstants:
    """Stores constants for Cart Page"""

    REMOVE_BUTTONS_XPATH = './/button[@class="basket-table__remove"]'
    EMPTY_LIST_MESSAGE_TEXT = 'Ваш кошик порожній!'


class CartPage(BasePage):
    """Representation of Catalog Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CartConstants
        self.header_bar = HeaderBar(self.driver)

    def remove_all_products(self):
        """Click on remove button of each product on the page"""

        products_count = len(self.get_elements(self.constants.REMOVE_BUTTONS_XPATH))
        for index in range(products_count):
            self.safe_click(self.constants.REMOVE_BUTTONS_XPATH + '[1]')
