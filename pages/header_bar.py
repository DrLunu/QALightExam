import enum

from pages.base_page import BasePage


class HeaderConstants:
    """Stores constants for Header Bar"""

    CATALOG_BUTTON_XPATH = './/nav[@class="nav"]//a[@href="#dropdown-catalog"]'
    PRODUCT_CATEGORY_XPATH = './/nav[@class="dropdown-categories"]//a[@href="https://darijewelry.com/{category}"]'

    CURRENCY_SELECT_XPATH = './/div[@class="header__right"]//span[@class="header-select__current"]'
    CURRENCY_XPATH = './/div[@class="header__right"]//a[@href="{currency}"]'

    CART_BUTTON_XPATH = './/li[@class="carts"]'

    UNAUTHORISED_PROFILE_BUTTON_XPATH = './/a[contains(text(),"Особистий кабінет")]'
    AUTHORISED_PROFILE_BUTTON_XPATH = './/div[@class="header__right"]//a[contains(text(),{username})]'


class ProductCategory(enum.Enum):
    """Defines product categories of Dari Jewelry web store"""

    ALL_PRODUCTS = "vsya-produkciya"
    EARRINGS = "serezhky"
    RINGS = "kablychki"
    PENDANTS = "kuloni"


class Currency(enum.Enum):
    """Defines currency symbols"""

    UAH = "грн"
    USD = "$"
    EUR = "€"


class HeaderBar(BasePage):
    """Representation of Header Bar"""

    def __init__(self, driver, user=None):
        super().__init__(driver)
        self.constants = HeaderConstants
        self.user = user

    def is_authorised(self) -> bool:
        """Returns True if HeaderBar is personalised for authorised user"""

        if self.user:
            return True
        else:
            return False

    @property
    def profile_button(self):
        """Returns profile button element according to authorisation status"""

        if self.is_authorised():
            return self.get_element(self.constants.AUTHORISED_PROFILE_BUTTON_XPATH.format(username=self.user.name))
        else:
            return self.get_element(self.constants.UNAUTHORISED_PROFILE_BUTTON_XPATH)

    def go_to_profile(self):
        """Clicks on profile button and returns ProfilePage or ProfileForm according to authorisation status"""

        self.profile_button.click()
        if self.is_authorised():
            from pages.profile_page import ProfilePage
            return ProfilePage(self.driver, self.user)
        else:
            from pages.login_form import LoginForm
            return LoginForm(self.driver)

    def go_to_catalog(self, category=ProductCategory.ALL_PRODUCTS):
        """Returns CatalogPage of certain category"""

        self.safe_click(self.constants.CATALOG_BUTTON_XPATH)
        self.safe_click(self.constants.PRODUCT_CATEGORY_XPATH.format(category=category.value))
        from pages.catalog_page import CatalogPage
        return CatalogPage(self.driver)

    def go_to_cart(self):
        """Clicks on cart button and returns CartPage"""
        self.safe_click(self.constants.CART_BUTTON_XPATH)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def change_currency(self, currency: Currency):
        """Set certain currency"""

        self.safe_click(self.constants.CURRENCY_SELECT_XPATH)
        self.safe_click(self.constants.CURRENCY_XPATH.format(currency=currency.name))
