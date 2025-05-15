from .base_page import BasePage
from .login_page import LoginPage
import pytest
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, CatalogPageLocators, ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*CatalogPageLocators.ADD_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message2(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"