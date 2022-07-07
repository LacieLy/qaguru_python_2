from selene import have, be
from selene.support.shared import browser


def test_right_search(open_google):
    query = browser.element('[name=q]')
    query.should(be.blank).type('Selene').press_enter()
    browser.element('#search').should(have.text('User-oriented Web UI browser tests in Python'))


def test_wrong_search(open_google):
    query = browser.element('[name=q]')
    query.should(be.blank).type('Wrongtext').press_enter()
    browser.element('#search').should(have.no.text('User-oriented Web UI browser tests in Python'))