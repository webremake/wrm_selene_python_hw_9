import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_control():
    browser.config.hold_browser_open = False
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = '1240'
    browser.config.window_height = '768'
    browser.config.timeout = 6.0
    yield
    browser.close()
    browser.quit()


