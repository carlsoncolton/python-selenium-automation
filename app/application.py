from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.cart_results_page import CartResultsPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.cart_results = CartResultsPage(driver)
