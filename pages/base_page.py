from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base functions of web page"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element(self, xpath: str, timeout=3) -> WebElement:
        """Returns element after searching by xpath with timeout"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_elements(self, xpath: str, timeout=3) -> [WebElement]:
        """Returns collection of elements after searching by xpath with timeout"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def is_element_presence(self, xpath: str, timeout=3) -> bool:
        """Returns True if can find element in timeout"""
        try:
            self.get_element(xpath, timeout)
            return True
        except TimeoutException:
            return False

    def is_message_presence(self, message: str, timeout=0, tag='*') -> bool:
        """Returns True if can find element containing message in timeout"""
        return self.is_element_presence(f'.//{tag}[contains(text(),"{message}")]', timeout)

    def safe_click(self, xpath: str, timeout=3):
        """Wait for element to be clickable and click on it"""
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    def fill_input(self, xpath: str, value='', timeout=3):
        """Sets value of text input"""
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.clear()
        element.send_keys(value)
