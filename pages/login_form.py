from entities.user import User
from pages.base_page import BasePage
from pages.header_bar import HeaderBar


class LoginFormConstants:
    """Stores constants for Login Form"""

    LOGIN_BUTTON_XPATH = '//button[@data-text="Увійти"]'
    PASSWORD_INPUT_XPATH = '//div[@id="modal-login"]//input[@name="password"]'
    EMAIL_INPUT_XPATH = '//div[@id="modal-login"]//input[@name="email"]'


class LoginForm(BasePage):
    """Representation of Login Form"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = LoginFormConstants
        self.header_bar = HeaderBar(self.driver)

    def login(self, user: User):
        """Fills login form and click Log In button"""

        self.fill_input(self.constants.EMAIL_INPUT_XPATH, user.email)
        self.fill_input(self.constants.PASSWORD_INPUT_XPATH, user.password)
        self.safe_click(self.constants.LOGIN_BUTTON_XPATH)

        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver, user)
