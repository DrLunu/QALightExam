from pages.base_page import BasePage
from pages.header_bar import HeaderBar


class ProductPageConstants:
    """Store constants for Product Page"""

    ADD_TO_CART_BUTTON_XPATH = './/a[@id="button-cart"]'
    ADDED_TO_CART_MESSAGE_TEXT = " до кошика"
    ADD_TO_WISHLIST_BUTTON_XPATH = './/div[@class="full-product__controls full-product__controls1"]//button'


class ProductPage(BasePage):
    """Representation of Product Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProductPageConstants
        self.header_bar = HeaderBar(self.driver)

    def add_to_cart(self):
        """Click on add to cart button"""

        self.safe_click(self.constants.ADD_TO_CART_BUTTON_XPATH)

    def add_to_wishlist(self):
        """Click on add to wishlist button and returns LoginForm if user is not authorised"""
        self.safe_click(self.constants.ADD_TO_WISHLIST_BUTTON_XPATH)
        if not self.header_bar.is_authorised():
            from pages.login_form import LoginForm
            return LoginForm(self.driver)
