import pytest
from selene.support.shared import browser


# Setting the window size to 1400 * 800
@pytest.fixture(scope='session', autouse=True)
def win_size():
    browser.config.window_width = 1400
    browser.config.window_height = 800


# Open Google.com
@pytest.fixture()
def open_google():
    browser.open('https://www.google.com/')