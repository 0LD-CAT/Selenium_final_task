from .base_page import BasePage
from .login_page import LoginPage
import pytest
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, CatalogPageLocators, ProductPageLocators, CartPageLocators

class BasketPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CartPageLocators.SUCCESS_MESSAGE), "Your basket is empty."\
            "Success message is presented, but should not be"

    def should_not_be_success_message2(self):
        assert self.is_disappeared(*CartPageLocators.SUCCESS_MESSAGE), "Your basket is empty."\
            "Success message is presented, but should not be"

    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)