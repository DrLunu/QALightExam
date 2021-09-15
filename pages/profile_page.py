from entities.user import User
from pages.base_page import BasePage
from pages.header_bar import HeaderBar


class ProfileConstants:
    """Stores constants for Profile Page"""

    LOGOUT_BUTTON_XPATH = './/a[@href="https://darijewelry.com/logout"]'
    WISHLIST_BUTTON_XPATH = './/ul/li/a[@href="https://darijewelry.com/wishlist"]'


class ProfilePage(BasePage):
    """Representation of Profile Page"""

    def __init__(self, driver, user: User):
        super().__init__(driver)
        self.constants = ProfileConstants
        self.user = user
        self.header_bar = HeaderBar(self.driver, user)

    def logout(self):
        """Clicks on logout button"""

        self.safe_click(self.constants.LOGOUT_BUTTON_XPATH, 3)
        from pages.start_page import StartPage
        return StartPage(self.driver)

    def go_to_wishlist(self):
        """Clicks on wishlist button"""

        self.safe_click(self.constants.WISHLIST_BUTTON_XPATH)
        from pages.wishlist_page import WishlistPage
        return WishlistPage(self.driver, self.user)

    def is_profile_page(self):
        """Returns True if current page is Profile Page"""

        return self.is_element_presence(self.constants.LOGOUT_BUTTON_XPATH, 3)
