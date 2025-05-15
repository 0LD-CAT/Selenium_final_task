from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver
import time

class LoginPage(BasePage):
    def setup_register(self):
        email = str(time.time()) + "@fakemail.org"
        print(email)
        self.register_new_user(email, 'o123456789o')
        self.should_be_authorized_user()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, \
            f"Должна быть ссылка {self.browser.current_url}/login/"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login from is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration from is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/input')
        input_email.send_keys(email)

        input_pass = self.browser.find_element(By.XPATH,
                                                '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div[2]/div/input')
        input_pass.send_keys(password)

        input_pass_again = self.browser.find_element(By.XPATH,
                                          '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div[3]/div/input')
        input_pass_again.send_keys(password)
        button = self.browser.find_element(By.XPATH,
                                      "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/button")
        button.click()