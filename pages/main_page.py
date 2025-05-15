from .base_page import BasePage
from .login_page import LoginPage
import pytest
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, CatalogPageLocators, ProductPageLocators, CartPageLocators

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)