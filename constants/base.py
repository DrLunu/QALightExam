class BaseConstants:
    """Contains basic constants for Dari Jewelry web store"""

    DRIVER_PATH = r'./drivers/chromedriver.exe'

    START_PAGE_URL = 'https://darijewelry.com/'
    TEST_PRODUCT_URL = 'https://darijewelry.com/kilze_storm_suniy_chorninna_schuroke'

    PRODUCT_XPATH = './/a[@href="{product_url}"]'
