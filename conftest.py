import pytest
from selene.support.shared import browser


@pytest.fixture()
def settings():
    browser.config.base_url = 'https://google.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def open_browser(settings):
    browser.open(browser.config.base_url)
    print('Открытие браузера с предустановками')
    yield
    browser.close()
    print('Закрытие браузера')