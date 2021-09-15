import pytest

from conftest import BaseTest
from constants.base import BaseConstants
from pages.header_bar import Currency


class TestDariJewelry(BaseTest):
    """Tests of Dari Jewelry web store"""

    def test_login(self, start_page, registered_user):
        """
        Pre-requirements:
            - Preregistered user
            - Open start page
        Steps:
            - Go to start page
            - Open login form
            - Login with preregistered user data
            - Verify profile page
        """
        login_form = start_page.header_bar.go_to_profile()
        self.log.info("Open login form")

        profile_page = login_form.login(registered_user)
        self.log.info("Login with cleared fields")

        assert profile_page.is_profile_page()
        self.log.info("Successful login")

    def test_logout(self, profile_page):
        """
        Pre-requirements:
            - Authorised user
            - Open profile page
        Steps:
            - Click on logout button
            - Verify logout
            - Verify start page
        """
        start_page = profile_page.logout()
        self.log.info("Click on logout button")

        assert not start_page.header_bar.is_authorised()
        assert start_page.is_start_page()
        self.log.info("Successful logout")

    @pytest.mark.parametrize('currency', [Currency.EUR, Currency.UAH, Currency.USD])
    def test_currency(self, start_page, currency):
        """
        Pre-requirements:
            - Open start page
        Steps:
            - Open products catalog
            - Change currency
            - Verify page changes
        """
        catalog_page = start_page.header_bar.go_to_catalog()
        self.log.info("Successful logout")

        catalog_page.header_bar.change_currency(currency=currency)
        self.log.info(f"Currency changed to {currency.name}")

        catalog_page.verify_currency(currency)
        self.log.info("Changes verified")

    def test_add_to_cart(self, test_product_page):
        """
        Pre-requirements:
            - Open product page
        Steps:
            - Click on add to cart button
            - Verify added message
            - Go to cart page
            - Verify product presence
            - Empty cart
            - Verify empty cart message
        """
        test_product_page.add_to_cart()
        self.log.info("Click on add to cart button")

        assert test_product_page.is_message_presence(test_product_page.constants.ADDED_TO_CART_MESSAGE_TEXT, 3, 'p')
        self.log.info("Message matches to expected")

        cart_page = test_product_page.header_bar.go_to_cart()
        self.log.info("Cart page is opened")

        product_url = BaseConstants.TEST_PRODUCT_URL
        assert cart_page.is_element_presence(BaseConstants.PRODUCT_XPATH.format(product_url=product_url))
        self.log.info("Product presence verified")

        cart_page.remove_all_products()
        assert cart_page.is_message_presence(cart_page.constants.EMPTY_LIST_MESSAGE_TEXT, 3, 'div')
        self.log.info("Cart is empty")

    def test_add_to_wishlist(self, test_product_page, registered_user):
        """
        Pre-requirements:
            - Preregistered user
            - Open product page
        Steps:
            - Click on add to wishlist button
            - Fill login form
            - Go to wishlist page
            - Verify product presence
            - Empty wishlist
            - Verify empty message
        """
        login_form = test_product_page.add_to_wishlist()
        self.log.info("Click on add to wishlist button")

        profile_page = login_form.login(registered_user)
        self.log.info("Login")

        wishlist_page = profile_page.go_to_wishlist()
        self.log.info("Wishlist is opened")

        product_url = BaseConstants.TEST_PRODUCT_URL
        assert wishlist_page.is_element_presence(BaseConstants.PRODUCT_XPATH.format(product_url=product_url))
        self.log.info("Product presence verified")

        wishlist_page.remove_all_products()
        assert wishlist_page.is_message_presence(wishlist_page.constants.EMPTY_LIST_MESSAGE_TEXT, 3, 'p')
        self.log.info("Wishlist is empty")
