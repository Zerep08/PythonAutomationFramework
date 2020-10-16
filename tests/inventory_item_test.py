from pages.login import LoginPage
from utilities.web_element_assert import element_is_displayed


def test_product_details(setup):
    login_page = LoginPage(setup["Driver"])
    inventory_page = login_page.actions.login(setup["UserName"], setup["Password"])
    inventory_item_page = inventory_page.actions.click_on_random_product()
    element_is_displayed(inventory_item_page.banner.swag_labs_label)
    element_is_displayed(inventory_item_page.banner.cart_icon)
    element_is_displayed(inventory_item_page.banner.burger_button)
