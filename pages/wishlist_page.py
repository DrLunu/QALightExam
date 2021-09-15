from entities.user import User
from pages.base_page import BasePage
from pages.header_bar import HeaderBar


class WishlistConstants:
    """Stores constants for Wishlist Page"""

    REMOVE_BUTTONS_XPATH = './/a[contains(text(),"Видалити")]'
    EMPTY_LIST_MESSAGE_TEXT = 'У вас ще немає вподобаних товарів'


class WishlistPage(BasePage):
    """Representation of Wishlist Page"""

    def __init__(self, driver, user: User):
        super().__init__(driver)
        self.constants = WishlistConstants
        self.header_bar = HeaderBar(self.driver, user)

    def remove_all_products(self):
        """Click on remove button of each product on the page"""

        products_count = len(self.get_elements(self.constants.REMOVE_BUTTONS_XPATH))
        for index in range(products_count):
            self.safe_click(self.constants.REMOVE_BUTTONS_XPATH + '[1]')
