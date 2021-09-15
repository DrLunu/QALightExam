from pages.base_page import BasePage
from pages.header_bar import HeaderBar, Currency
from utils.decorators import retry_till_success


class CatalogConstants:
    """Stores constants for Catalog Page"""

    PRODUCT_PRICES_XPATH = './/div/span[@class="product-card__price"][1]'


class CatalogPage(BasePage):
    """Representation of Catalog Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CatalogConstants
        self.header_bar = HeaderBar(self.driver)

    @retry_till_success()
    def verify_currency(self, currency: Currency):
        """Chek currency symbol of each product on the page"""

        prices = self.get_elements(self.constants.PRODUCT_PRICES_XPATH)
        result = True
        for price in prices:
            price_str = str(price.text)
            result = price_str.find(currency.value)
            if result == -1:
                result = False
                break
        assert result
