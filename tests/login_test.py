from pages.login import LoginPage


def test_successfully_login(setup):
    login_page = LoginPage(setup["Driver"])
    login_page.actions.login(setup["UserName"], setup["Password"]) \
        .inventory_page_should_be_displayed()


def test_invalid_login(setup):
    login_page = LoginPage(setup["Driver"])
    login_page.actions.login(setup["InvalidUser"], setup["Password"])
    login_page.actions.error_displayed_for_invalid_login()
