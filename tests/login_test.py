from pages.login import LoginPage
from utilities.web_element_assert import element_is_displayed, element_list_is_not_empty, element_is_equal_to_text


def test_successfully_login(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    element_is_displayed(inventory_page.banner.swag_labs_label)
    element_is_displayed(inventory_page.banner.peek_icon)
    element_is_displayed(inventory_page.sort_drop_down)
    element_is_displayed(inventory_page.banner.cart_icon)
    element_is_displayed(inventory_page.footer)
    element_list_is_not_empty(inventory_page.product_list)


def test_invalid_login(setup):
    login_page = LoginPage(setup["Driver"])
    login_page.actions.login(setup["InvalidUser"], setup["Password"])
    element_is_displayed(login_page.login_error)
    element_is_equal_to_text(login_page.login_error, "Epic sadface: Sorry, this user has been locked out.")
