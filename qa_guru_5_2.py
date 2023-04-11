from selene.support.shared import browser
from selene import be, have

import generate_random_strings


def test_google_should_find_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_should_not_find_something(open_browser):
    browser.element('[name="q"]').should(be.blank).type(generate_random_strings.random_string(30)).press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
