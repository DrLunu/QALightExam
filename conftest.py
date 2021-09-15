import logging
import pytest
from selenium import webdriver

from constants.base import BaseConstants
from entities.user import User
from pages.product_page import ProductPage
from pages.start_page import StartPage


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)


class BaseTest:
    log = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def driver():
    """Returns Chrome web driver"""
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1500,800')
    driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH, options=options)
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def registered_user():
    """Returns preregistered User"""
    yield User.get_registered_user()


@pytest.fixture(scope="function")
def start_page(driver):
    """Returns StartPage object and clears cookie files after test"""
    driver.get(BaseConstants.START_PAGE_URL)
    yield StartPage(driver)
    driver.delete_all_cookies()


@pytest.fixture(scope="function")
def profile_page(start_page, registered_user):
    """Returns ProfilePage"""
    login_form = start_page.header_bar.go_to_profile()
    profile_page = login_form.login(registered_user)
    yield profile_page


@pytest.fixture(scope="function")
def test_product_page(driver):
    """Returns ProductPage"""
    driver.get(BaseConstants.TEST_PRODUCT_URL)
    yield ProductPage(driver)
