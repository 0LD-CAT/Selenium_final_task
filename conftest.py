import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     choices=['chrome', 'firefox'],
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose interface language (e.g., 'en', 'ru', 'fr', 'es', 'de', etc.)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print(f"\nStarting Chrome browser with {user_language} language...")
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option('prefs', {
            'intl.accept_languages': user_language,
            'profile.default_content_setting_values.popups': 0
        })
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print(f"\nStarting Firefox browser with {user_language} language...")
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        options.set_preference("dom.webnotifications.enabled", False)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(5)
    yield browser

    print("\nClosing browser...")
    browser.quit()